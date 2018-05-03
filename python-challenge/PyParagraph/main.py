import os
import csv
import re

ParaPath = os.path.join("PyParagraph","Resources","paragraph_1.txt")

with open(ParaPath, newline="") as Parafile:
    reader = csv.reader(Parafile)
    for row in reader:
        data= list(reader)
        re.split("(?&lt;=[.!?])+", row)
