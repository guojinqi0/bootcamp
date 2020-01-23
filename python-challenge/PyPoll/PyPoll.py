import os
import csv
import collections

# Path to collect data from the resources folder
poll_path=os.path.join('Resources','election_data.csv')

# open the csv file
with open (poll_path,'r') as poll_csv:
    poll_file=csv.reader(poll_csv,delimiter=',')
# skip the header row
    next(poll_file)
# convert candidate column into a list
    votes=[]
    for row in poll_file:
        votes.append(row[2])
# The total number of votes cast
        totalvotes=0
        totalvotes=len(votes)

# A complete list of candidates who received votes
    candidatelist=[]
    for candidate in votes:
        if candidate not in candidatelist:
            candidatelist.append(candidate)

# The total number of votes each candidate won
    CountOfVotes=collections.Counter(votes)
# convert the values in dict to a list for further calculation
    votecounts=list(CountOfVotes.values())
  
# To start the iteration again
    poll_csv.seek(0)
# skip the header row again
    next(poll_file)
# The percentage of votes each candidate won
    votePercentage=[]
    for i in range(len(votecounts)):
        def percent(votecounts):
            percentage="{:.3%}".format(votecounts[i]/totalvotes)
            return percentage
        votePercentage.append(percent(votecounts))

# The winner of the election based on popular vote.
    max_vote = max(votecounts)
    max_index=votecounts.index(max_vote)
    winner=candidatelist[max_index]
   
# print results
print ("Election Results")
print("-------------------------")
print (f'Total Votes: {totalvotes}')
print ("-------------------------")
for i in range(len(candidatelist)):
    print(f'{candidatelist[i]}: {votePercentage[i]} ({votecounts[i]})')
print ("-------------------------")
print (f'Winner: {winner}')
print ("-------------------------")

# Specify the file to write to
output_path = os.path.join("PollResult.txt")
with open(output_path, 'w') as PollResult:

    # Write contents
    print ("Election Results", file=PollResult)
    print("-------------------------", file=PollResult)
    print (f'Total Votes: {totalvotes}', file=PollResult)
    print ("-------------------------", file=PollResult)
    for i in range(len(candidatelist),):
        print(f'{candidatelist[i]}: {votePercentage[i]} ({votecounts[i]})', file=PollResult)
    print ("-------------------------", file=PollResult)
    print (f'Winner: {winner}', file=PollResult)
    print ("-------------------------", file=PollResult)

