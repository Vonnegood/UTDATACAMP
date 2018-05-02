'''
Average Revenue Change needs work
'''


import os
import csv

# Path to the files
Bankcsv1 = os.path.join("PyBank","Resources","budget_data_1.csv")
Bankcsv2 = os.path.join("PyBank","Resources","budget_data_2.csv")

# Variables for the report
Periods = 0
Total_Revenue = 0
Avg_RevChange = 0.0
Great_Inc = ["A","0"]
Great_Dec = ["A","0"]
Delta = 0.0
prev_month = "A"

with open(Bankcsv1, newline="") as Budgetfile1:
    reader = csv.reader(Budgetfile1)
    next(reader, None)
    data = list(reader)
    Periods = len(data) # Months
    for row in data:
        cur_month = int(row[1])
        Total_Revenue += int(row[1])

        if int(row[1]) > int(Great_Inc[1]):
            Great_Inc = row
        elif int(row[1]) < int(Great_Dec[1]):
            Great_Dec = row
        # Average Revenue Change: skip the first row
        if prev_month == "A" and Total_Revenue == int(row[1]):
            prev_month = int(row[1])
            continue
        else: 
            Delta += (cur_month - prev_month) / 2
            prev_month = int(row[1]) # Revenue Change
            print(Delta)

Avg_RevChange = Delta / (int(Periods)-1)

print(Avg_RevChange)

# print("Financial Analysis \n ----------------------------")
# print("Total Months: "+ str(Periods))
# print("Total Revenue: $"+ str(Total_Revenue))
# print(f"Average Revenue Change: ${Avg_RevChange}")
# print(f"Greatest Increase in Revenue: {Great_Inc[0]} (${Great_Inc[1]})")
# print(f"Greatest Decrease in Revenue: {Great_Dec[0]} (${Great_Dec[1]})")
