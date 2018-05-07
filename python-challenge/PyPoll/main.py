import os
import csv

# Filepaths
file_name= input("Please input the file name that has been placed in the 'raw_data' folder.\n    (Don't include the .csv. I'll add that):")
csv_file = f"{file_name}.csv"
filepath = os.path.join("raw_data",csv_file)
txt_file = f"{file_name}_output.txt"
outputpath = os.path.join("Output",txt_file)

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
        if Candidates[candidate] > winning_amount:
            winner = candidate
            winning_amount = Candidates[candidate]

    print("Election Results \n------------------------\n")
    print(f"Total Votes: {total_votes}\n------------------------\n")
    for candidate in Candidates:
        percent_votes = Candidates[candidate] / total_votes * 100
        percent_votes = round(percent_votes, 1)
        print(f"{candidate} {percent_votes}% ({Candidates[candidate]})\n")
    print("-------------------------\n")
    print(f"Winner: {winner}\n-------------------------\n")

output = open(outputpath,"w")
output.write("Election Results \n------------------------\n")
output.write(f"Total Votes: {total_votes}\n------------------------\n")
for candidate in Candidates:
    percent_votes = Candidates[candidate] / total_votes * 100
    percent_votes = round(percent_votes, 1)
    output.write(f"{candidate} {percent_votes}% ({Candidates[candidate]})\n")
output.write("-------------------------\n")
output.write(f"Winner: {winner}\n-------------------------\n")