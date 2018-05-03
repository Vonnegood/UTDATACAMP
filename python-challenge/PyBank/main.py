'''
Export to file needs work

Assumptions: There will never be a duplicate line for month-year combo
             Data is held in the same manner in the files
             
'''


import os
import csv

# Path to the files
Bankcsv1 = os.path.join("PyBank","Resources","budget_data_1.csv")
Bankcsv2 = os.path.join("PyBank","Resources","budget_data_2.csv")
output_path = os.path.join("output","PyBankOutput.txt")

# Variables for the report
Periods = 0
Total_Revenue = 0
Avg_RevChange = 0.0
Great_Inc = ["A","0"]
Great_Dec = ["A","0"]
Delta = 0.0
Delta_Total = 0.0
prev_month = "A"

with open(Bankcsv1, newline="") as Budgetfile1:
    reader = csv.reader(Budgetfile1)
    next(reader, None)
    data = list(reader)
    Periods = len(data) # Months
    for row in data:
        cur_month = int(row[1])
        Total_Revenue += int(row[1])

        # Average Revenue Change: skip the first row
        if prev_month == "A" and Total_Revenue == int(row[1]):
            prev_month = int(row[1]) #break out of the first loop
            continue
        else: 
            Delta = (cur_month - prev_month) 
            Delta_Total += Delta #Save the total Revenue Change for averaging later
            prev_month = int(row[1]) # Revenue Change
        
        # save the greatest inc/dec into variable
        if Delta > int(Great_Inc[1]):
            Great_Inc = [row[0],Delta]
        elif Delta < int(Great_Dec[1]):
            Great_Dec = [row[0],Delta]

Avg_RevChange = Delta_Total / (int(Periods)-1)

# Write the file
#with open(output_path, 'w', newline="") as output:
#    csvwriter = csv.writer(output)
print("Financial Analysis \n ----------------------------")
print("Total Months: "+ str(Periods))
print("Total Revenue: $"+ str(Total_Revenue))
print(f"Average Revenue Change: ${Avg_RevChange}")
print(f"Greatest Increase in Revenue: {Great_Inc[0]} (${Great_Inc[1]})")
print(f"Greatest Decrease in Revenue: {Great_Dec[0]} (${Great_Dec[1]})")

