# First we'll import the os module
# This will allow us to create file paths across operating systems
#import budget data
import os

# Module for reading CSV files
import csv

csvpath = os.path.join("/Users/sanitagurung/Desktop/KU-OVE-DATA-PT-01-2020-U-C/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")

#Declare Variables
khan_votes =0
correy_votes =0
li_votes = 0
otooley_votes = 0
total_votes = 0

# Open csv in default read mode with context manager
with open(csvpath, newline="",) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# Read each row of data after the header
#months and total profit to theor corresponding lists
    for row in csvreader:
       
        # Count the unique Voter ID's and store in variable  called total_votes
        total_votes +=1

        #Using the values to calculate percent vote in the print statement
        if row[2] == "Khan":
                khan_votes +=1
        elif row[2] == "Correy":
                correy_votes +=1
        elif row[2] == "Li":
                li_votes +=1
        elif row[2] == "O'Tooley":
                otooley_votes +=1
#complete list of candidates who received votes
votes = [khan_votes, correy_votes, li_votes, otooley_votes]
candidates = ["Khan", "Correy", "Li", "O'Tooley"]

# We zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

#The percentage of votes each candidate
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

#Output files
output_file = os.path.join("Election_Results_Summary.txt")


with open(output_file,"w") as txtfile:
        election_results = (f"\n\nElection Results\n"
                f"Total Votes: {total_votes}\n"
                f"Khan: {khan_percent:.3f}% ({khan_votes})\n"
                f"Correy: {correy_percent:.3f}% ({correy_votes})\n"
                f"Li: {li_percent:.3f}% ({li_votes})\n"
                f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})\n"
                f"----------------------------"
                f"Winner: {key}\n"
                f"----------------------------")

        txtfile.write(election_results)




# Write methods to print to Elections_Results_Summary 
# Print the summary table

print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")


