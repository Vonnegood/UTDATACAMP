'''
Need to work on removing the double-quotes from 'words'


'''
import os
import csv
import re

ParaPath = os.path.join("PyParagraph","Resources","example.txt")

sentences = []
Total_word_len = 0
avg_word_len = 0.0
Total_sent_len = 0.0
avg_sent_len = 0.0

with open(ParaPath, newline="") as Parafile:
    reader = csv.reader(Parafile)
    Text = Parafile.read()
    # print(Text)
    sentences = re.split("(?<=[.!?]) +", Text)
    words = Text.split(" ") # Split sentence into words
    for word in words: # to compute the average letter count per word
        word_len = len(word)
        Total_word_len += word_len
    avg_word_len = Total_word_len / len(words)
    for sentence in sentences:
        sentence_split = sentence.split(" ")
        Total_sent_len += len(sentence_split)
    avg_sent_len = Total_sent_len/len(sentences)



    
    
print(words[101]) # Is frock-coat one or two words?

print("Paragraph Analysis \n -----------------")
print(f"Approximate Word Count: {len(words)}")
print(f"Approcimate Sentence Count: {len(sentences)}")
print(f"Average Letter Count: {avg_word_len}")
print(f"Average Sentence Length: {avg_sent_len}")
