import os
import csv

# Filepaths
filepath = os.path.join("raw_data","election_data_1.csv")
outputpath = os.path.join("Output","poll.txt")

# Variables
Candidates = {}
total_votes = 0
percent_votes = 0.0
winning_amount = 0

with open(filepath, newline="") as electiondata:
    reader = csv.DictReader(electiondata)
    for row in reader:
        count = 1 # to increment total votes
        candidate = row["Candidate"]
        if candidate in Candidates: # If already in list add one to vote total
            Candidates[candidate] +=1
        else:                       # Otherwise create candidate key with one vote
            Candidates[candidate] = 1
        total_votes += count
    for candidate in Candidates: # Percentage of Votes & Winner determination
        percent_votes = Candidates[candidate] / total_votes * 100
        percent_votes = round(percent_votes, 1)
        if Candidates[candidate] > winning_amount:
            winner = candidate
            winning_amount = Candidates[candidate]

    print("Election Results \n------------------------\n")
    print(f"Total Votes: {total_votes}\n------------------------\n")
    for candidate in Candidates:
        print(f"{candidate} {percent_votes}% ({Candidates[candidate]})\n")
    print("-------------------------\n")
    print(f"Winner: {winner}\n-------------------------\n")

output = open(outputpath,"w")
output.write("Election Results \n------------------------\n")
output.write(f"Total Votes: {total_votes}\n------------------------\n")
for candidate in Candidates:
    output.write(f"{candidate} {percent_votes}% ({Candidates[candidate]})\n")
output.write("-------------------------\n")
output.write(f"Winner: {winner}\n-------------------------\n")