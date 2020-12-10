#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 18:13:06 2020

@author: Kevin
"""

# -*- coding: utf-8 -*-
"""
This is the script for the poll part of python homework.
It reads a csv file, then manipulates the data in a loop to count
    The total votes
    The votes/percentage of votes each candidate got
    The winner
    Not required, but added:  I threw in a QA check to see if any other candidates got votes.

This script became easier to visualize after mocking up the columns and calculations in excel

The part at the end to write to file is garbage code, but it works.
"""
# A quick function to print my dashed lines
def printDashes():
    print()
    print("----------------------------------")
    print()

import csv
import sys
import os
#Define variables
voterCount = 0

khanVote = 0
khanPercent = 0
correyVote = 0
correyPercent = 0
liVote = 0
liPercent = 0
liArray = ["Li", liVote, liPercent]
tooleyVote = 0
tooleyPercent = 0
tooleyArray = ["O'Tooley", tooleyVote,tooleyPercent]
otherVote = 0
otherPercent = 0
winner = 0
winnerName = ""
outputFile = 'Analysis/Poll Results.txt'

filePath = 'Resources/ElectionData.csv'
outputFile = 'Analysis/PollResults.txt'

with open(filePath, 'r') as csvfile:
    data = csv.reader(csvfile) #Dump the entire file into the variable DATA
    next(data)  #skips the header line (Row 1 in Excel)
#   Loops through rows 2 to end of file
    for row in data:
        voterCount = voterCount + 1 #count the total votes
        if row[2]=="Khan":
            khanVote = khanVote + 1 # count the individual votes
        elif row[2] == "Correy":
            correyVote = correyVote + 1
        elif row[2] == "Li":
            liVote = liVote + 1
        elif row[2] == "O'Tooley":
            tooleyVote = tooleyVote + 1
        else:
            otherVote = otherVote + 1

    khanPercent = (khanVote/voterCount) * 100
    correyPercent = (correyVote/voterCount) * 100
    liPercent = (liVote/voterCount) * 100
    tooleyPercent = (tooleyVote/voterCount) * 100
    otherPercent = (otherVote/voterCount) * 100

winner = max(khanVote,correyVote,liVote,tooleyVote)

if winner == khanVote:
	winnerName = "Khan"
elif winner == correyVote:
    winnerName = "Correy"
elif winner == liVote:
    winnerName = "Li"
else:
    winnerName == "O'Tooley"

print("Election Results")
printDashes()
print("Total Votes:\t",voterCount)
printDashes()
print("Candidate\tPercentage\tVotes")
printDashes()
print(("Khan:\t\t"+"{:.3f}").format(khanPercent)+"%\t\t",khanVote)
print(('Correy:\t\t'+"{:.3f}").format(correyPercent)+"%\t\t", correyVote)
print(("Li:\t\t\t"+"{:.3f}").format(liPercent)+"%\t\t",liVote)
print(("O'Tooley:\t"+"{:.3f}").format(tooleyPercent)+"%\t\t",tooleyVote)
print(("Other:\t\t"+"{:.3f}").format(otherPercent)+"%\t\t",otherVote)
printDashes()
print("Winner:\t", winnerName)
printDashes()


stdoutOrigin=sys.stdout
txtPath = os.path.join("Analysis", "PollResults.txt")
sys.stdout = open(txtPath, "w")

print("Election Results")
print("\n----------------------------------------\n")
print("Total Votes: ", voterCount)
print("\n----------------------------------------\n")
print("Candidate\tPercentage\tVotes")
print("\n----------------------------------------\n")
print("Khan:\t\t", "{:.3f}".format(khanPercent)+"%\t", khanVote)
print("Correy:\t\t", "{:.3f}".format(correyPercent)+"%\t", correyVote)
print("Li:\t\t", "{:.3f}".format(liPercent)+"%\t", liVote)
print("O'Tooley:\t", "{:.3f}".format(tooleyPercent)+"%\t\t", tooleyVote)
print("\n----------------------------------------\n")
print("Winner: ", winnerName)
print("\n----------------------------------------\n")
sys.stdout.close()
sys.stdout=stdoutOrigin
