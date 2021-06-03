import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
csvpath = os.getcwd() + '\\' + os.path.join('PyBank', 'Resources', 'budget_data.csv')
# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))
total_months = 0
total_net = 0.0
change = 0.0
net_change = []
biggest_loss = 0.0
biggest_gain = 0.0
# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)

    print(csvreader)

    

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    jan_data = next(csvreader)
    total_months = total_months + 1
    total_net = total_net + int(jan_data[1])
    prev_change = int(jan_data[1])
    
    # Read each row of data after the header
    for row in csvreader:
        # print(row)
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        change = int(row[1]) - prev_change
        if change >biggest_gain:
            biggest_gain = change
        if change < biggest_loss:
            biggest_loss = change
        prev_change = int(row[1])
        net_change.append(change)
    
average_change = sum(net_change)/len(net_change)
#print(total_months, total_net, average_change)
        
print('Total Months: ' + str(total_months))
print("Average  Change: " + "(${:,.2f})".format(average_change))
print("Greatest profit loss:" + "$(" + str(biggest_loss) + ")")
print("Greatest profit Gain:" + "$(" + str(biggest_gain) + ")")
