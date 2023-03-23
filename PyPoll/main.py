import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    # The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
    # Your task is to create a Python script that analyzes the votes and 
    # calculates each of the following values:
    # The total number of votes cast
    total_votes = 0
    candidate_votes = {}
    for row in csvreader:
        # Count the total number of votes cast
        total_votes += 1
        
        # A complete list of candidates who received votes
        #The total number of votes each candidate won
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
    
    # Your analysis should align with the following results:
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    # #The percentage of votes each candidate won
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")

    print("-------------------------")

    # The winner of the election based on popular vote
    winner = max(candidate_votes, key=candidate_votes.get)
    print(f"Winner: {winner}")

    print("-------------------------")
    # Election Results
    # -------------------------
    # Total Votes: 369711
    # -------------------------
    # Charles Casper Stockham: 23.049% (85213)
    # Diana DeGette: 73.812% (272892)
    # Raymon Anthony Doane: 3.139% (11606)
    # -------------------------
    # Winner: Diana DeGette
    # -------------------------
    # Export a text file with the results
    with open("Analysis/pypoll.txt", "w") as txtfile:
        txtfile.write("Election Results\n")
        txtfile.write("-------------------------\n")
        txtfile.write(f"Total Votes: {total_votes}\n")
        txtfile.write("-------------------------\n")
        for candidate in candidate_votes:
            votes = candidate_votes[candidate]
            percentage = (votes / total_votes) * 100
            txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        txtfile.write("-------------------------\n")
        txtfile.write(f"Winner: {winner}\n")
        txtfile.write("-------------------------\n")
