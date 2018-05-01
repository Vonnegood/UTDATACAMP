import os
import csv

Bankcsv1 = os.path.join("PyBank","Resources","budget_data_1.csv")
Bankcsv2 = os.path.join("PyBank","Resources","budget_data_2.csv")

with open(Bankcsv1, newline="") as Budgetfile1:
    reader = csv.reader(Budgetfile1)
    for row in reader:
        print(row)