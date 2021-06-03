import os

# Module for reading CSV files
import csv

csvpath = os.getcwd() + '\\' + os.path.join('PyPoll', 'Resources', 'election_data.csv')



# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


total_votes = 0
candidates = []
candidate_votes = []
# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        # row_temp = row.split(",")
        row_ID = int(row[0])
        row_county = row[1]
        row_candidate = row[2]
        if row_candidate in candidates:
            ind = candidates.index(row_candidate)
            candidate_votes[ind]+=1
        else:
            candidates.append(row_candidate)
            candidate_votes.append(1)
        total_votes+=1
    

max_value = 0
max_ind = 0
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
for can in range(len(candidates)):
    print(candidates[can] + ": " + "{:,.3f}".format(candidate_votes[can]/total_votes * 100) + "% (" + str(candidate_votes[can]) + ")")
    if max_value < candidate_votes[can]:
        max_value = candidate_votes[can]
        max_ind = can
print("-------------------------")
print("Winner: " + candidates[max_ind])
print("-------------------------")
        