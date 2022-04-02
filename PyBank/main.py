# PyBank main

# import dependencies
import csv
import os

dates = []
changes = []
pre_mon = 0

# pathway into csv file
csvpath = os.path.join("Resources","budget_data.csv")

# pathway out to csv file
output_path = os.path.join("Analysis","analysis.txt")

# Step 1: read in csv X
# Step 2: initializations X 
    # Step 2.1: initialize dates list, dates = [] X
    # Step 2.2: initialize prev_mon = 0 X
    # Step 2.3: initialize changes list, changes = [] X
# Step 3: go through the loop X
    # Step 3.1: pull dates out of the row of the csv X
        # Step 3.1.1: pull the date from the 0th row position, row[0] X
        # Step 3.1.2: append date to dates X
    # Step 3.2: determine the change from month to month X
        # Step 3.2.1: pull amount from 1st column position, row[1] 
        # Step 3.2.2: append amount to cur_mon X
        # Step 3.2.3: subtract cur_mon - prev_mon to get change X
        # Step 3.2.4: cur_mon becomes prev_mon X
        # Step 3.2.5: append change to changes list X
# Step 4: calculate average of change
# Step 5: 


# Read in csv 
with open(csvpath, encoding = "UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvfile)

    for row in csvreader:
        date = row[0]
        dates.append(date)

        cur_mon = int(row[1])
        change = cur_mon - pre_mon
        pre_mon = cur_mon
        changes.append(change)

    avg = sum(changes) / len(changes)

with open(output_path, 'w') as text:
    text.writelines("Financial Analysis\n")
    text.writelines("-------------------------------\n")
    text.writelines(f"Total months: {len(changes)}\n")
    text.writelines(f"Total: ${sum(changes)}\n")
    text.writelines(f"Average change: ${round(avg,0)}\n")
    text.writelines(f"Greatest increase in profit : ${max(changes)}\n")
    text.writelines(f"Greatest decrease in profit : ${min(changes)}\n")

print("Financial Analysis")
print("-------------------------------")
print(f"Total months: {len(changes)}")
print(f"Total: ${sum(changes)}")
print(f"Average change: ${round(avg,0)}")
print(f"Greatest increase in profit : ${max(changes)}")
print(f"Greatest decrease in profit : ${min(changes)}")