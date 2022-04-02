# PyPoll main

# import dependencies
import csv
import os

BallotBox = []
StockhamVotes = []
DeGetteVotes = []
DoaneVotes = []

# Pathway into file
csvpath = os.path.join("Resources","election_data.csv")

# Pathway to output file
output_path = os.path.join("Analysis","results.txt")

# Step 1: read in csv 
with open(csvpath, encoding = "UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvfile)

    for row in csvreader:
        # Put the ballot in the box
        ballot = row[0]
        BallotBox.append(ballot)

        # Count the votes for each candidate and put them in their list
        if row[2] == "Charles Casper Stockham":
            CVote = row[0]
            StockhamVotes.append(CVote)
        elif row[2] == "Diana DeGette":
            DVote = row[0]
            DeGetteVotes.append(DVote)
        elif row[2] == "Raymon Anthony Doane":
            RVote = row[2]
            DoaneVotes.append(RVote)
    
    # Calcluate percentage of votes
    DeGettePercent = round(len(DeGetteVotes)/len(BallotBox) * 100,3)
    StockhamPercent = round(len(StockhamVotes)/len(BallotBox) * 100,3)
    DoanePercent = round(len(DoaneVotes)/len(BallotBox) * 100,3)

    # Determine the winner
    winner = "none"
    while winner == "none":
        if DeGetteVotes.count(DVote) > StockhamVotes.count(CVote) & DoaneVotes.count(RVote):
            winner = "Diana DeGette"
        elif StockhamVotes.count(CVote) > DeGetteVotes.count(DVote) & DoaneVotes.count(RVote):
            winner = "Charles Casper Stockham"
        else:
            winner = "Raymon Anthony Doan"

# Print to .txt file
with open(output_path, 'w') as text:
    text.writelines("Election Results\n")
    text.writelines("-------------------------------\n")
    text.writelines(f"Total votes: {len(BallotBox)} votes\n")
    text.writelines("-------------------------------\n")
    text.writelines(f"Charles Casper Stockham : {len(StockhamVotes)} votes ({StockhamPercent}%)\n")
    text.writelines(f"Diana DeGette : {len(DeGetteVotes)} votes ({DeGettePercent}%)\n")
    text.writelines(f"Raymon Anthony Doane : {len(DoaneVotes)} votes ({DoanePercent}%)\n")
    text.writelines("-------------------------------\n")
    text.writelines(f"Winner: {winner}\n")
    text.writelines("-------------------------------\n")

# Print to terminal
print("Election Results\n")
print("-------------------------------\n")
print(f"Total votes: {len(BallotBox)} votes\n")
print("-------------------------------\n")
print(f"Charles Casper Stockham : {len(StockhamVotes)} votes ({StockhamPercent}%)\n")
print(f"Diana DeGette : {len(DeGetteVotes)} votes ({DeGettePercent}%)\n")
print(f"Raymon Anthony Doane : {len(DoaneVotes)} votes ({DoanePercent}%)\n")
print("-------------------------------\n")
print(f"Winner: {winner}\n")
print("-------------------------------\n")