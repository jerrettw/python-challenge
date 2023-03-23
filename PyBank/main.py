import os
import csv

total_months = []
net_prof_loss = []
avg_prof_loss = []
greatest_increase = ['', 0]
greatest_decrease = ['', 0]

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    previous_pl = 0
    for row in csvreader:
        # Your task is to create a Python script that analyzes the records to 
        # calculate each of the following values:
        # 1. The total number of months included in the dataset
        total_months.append(row[0])
        count_tm = len(total_months)

        # 2. The net total amount of "Profit/Losses" over the entire period
        net_prof_loss.append(int(row[1]))
        sum_net_pl = sum(net_prof_loss)

        # 3. The changes in "Profit/Losses" over the entire period, and then the average of those changes
        current_pl = int(row[1])
        pl_change = current_pl - previous_pl
        previous_pl = current_pl

        avg_prof_loss.append(pl_change)

        # 4. The greatest increase in profits (date and amount) over the entire period
        if pl_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = pl_change
        # 5. The greatest decrease in profits (date and amount) over the entire period
        if pl_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = pl_change

# 3. The average of the changes in "Profit/Losses" over the entire period
avg_prof_loss = sum(avg_prof_loss) / len(avg_prof_loss)

# In addition, your final script should both print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {count_tm}")
print(f"Total: ${sum_net_pl}")
print(f"Average Change: ${avg_prof_loss:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
# and export a text file with the results
with open("Analysis/pybank.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {count_tm}\n")
    file.write(f"Total: ${sum_net_pl}\n")
    file.write(f"Average Change: ${avg_prof_loss:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
# Your analysis should align with the following results:
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)