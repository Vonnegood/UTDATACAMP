'''
Need to work on removing special characters from 'words'

'''
import os
import csv
import re

ParaPath = os.path.join("PyParagraph","Resources","example.txt")

sentences = []
sentences_clean = []
Total_word_len = 0
avg_word_len = 0.0
Total_sent_len = 0.0
avg_sent_len = 0.0


with open(ParaPath, newline="") as Parafile:
    reader = csv.reader(Parafile)
    Text = Parafile.read()
    #print(Text)
    sentences = re.split("(?<=[.!?]) +", Text)
    for sentence in sentences: # To clean words from special characters & find the length of sentences
        nstr = re.sub(r'[?|$|.|!|,|-]',r'',sentence)
        sentences_clean.append(nstr)
        sentence_split = sentence.split(" ")
        Total_sent_len += len(sentence_split)

    # Create a single list for words
    clean_text = re.sub(r'[?|$|.|!|,|-]',r'',Text)
    words = clean_text.split(" ")
    for word in words:
        Total_word_len += len(word)

    avg_sent_len = Total_sent_len/len(sentences)
    avg_word_len = Total_word_len / len(words)

print("Paragraph Analysis \n -----------------")
print(f"Approximate Word Count: {len(words)}")
print(f"Approximate Sentence Count: {len(sentences)}")
print(f"Average Letter Count: {avg_word_len}")
print(f"Average Sentence Length: {avg_sent_len}")
