#Dependencies
import os
import csv

#Specify folder and csv to read. Specify folder and csv to output analysis.
csvpath = os.path.join('Resources','election_data.csv')
output_path = os.path.join('analysis','analysis.txt')

with open (csvpath, 'r') as csv_file:
    csv_reader= csv.reader(csv_file)
    csv_header=next(csv_reader)
    
    #Set variables to blank
    totalvotes = []
    candidates = []

    for row in csv_reader:
        totalvotes.append(row[0])
        candidates.append(row[2])
    
    #Find all unique candidates
    unique_candidates=[]
    for x in candidates:
        if x not in unique_candidates:
            unique_candidates.append(x)
          

f=open(output_path, "w")
print("Election Results")
print("Election Results", file=f)
print("-----")
print("-----", file=f)
print("Total Votes:", len(totalvotes))
print("Total Votes:", len(totalvotes), file=f)
print("-----")
print("-----", file=f)
total_vote_count= len(totalvotes)

def CandidateResults(unique_candidate, total_vote_number, candidates):
    candidate_votes= candidates.count(unique_candidate)
    candidate_percent= round(100 * candidate_votes / total_vote_number, 3)
    print(unique_candidate, ": ", candidate_percent, "% ",'(',candidate_votes, ')\n',sep="", end="")
    output=f'{unique_candidate}: {candidate_percent}% {candidate_votes}\n'
    print(output, file=f)

CandidateResults(unique_candidates[0], total_vote_count, candidates)
CandidateResults(unique_candidates[1], total_vote_count, candidates)
CandidateResults(unique_candidates[2], total_vote_count, candidates)

#create dictionary for candidates and votes
candidate_votes = {}
for name in unique_candidates:
    votes = candidates.count(name)
    candidate_votes[name] = votes

#find winner
winner_name= list(candidate_votes.keys())[0]
for name in candidate_votes:
        if candidate_votes[name] > candidate_votes[winner_name]:
            winner_name= name

print("-----")
print("-----", file=f)
print(f"Winner: {winner_name}")
print(f"Winner: {winner_name}", file=f)
print("-----")
print("-----", file=f)