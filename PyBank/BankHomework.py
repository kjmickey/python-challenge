# -*- coding: utf-8 -*-
"""
This is the script for the banking part of python homework.
It reads a csv file, then manipulates the data in a loop to count
    how many months are covered
    how much money they made/lost
    average profit/loss each month
    Which month showed greatest increase in profit
    Which month showed greatest losses

This script became easier to visualize after mocking up the columns and calculations in excel

The part at the end to write to file is garbage code, but it works.
"""

import csv

#Define variables just to track them
totalEarnings = 0
monthCount = 0
previousRow = 0
monthlyDelta = 0
totalDelta = 0
averageChange = 0.0
theBiggest = 0
smallestMonth = ["Smallest",10];
biggestMonth = ["Biggest",20];
theSmallest = 0
outputFile = "Analysis/P and L Statement.txt"
title = "Financial Analysis \n------------------------------\n\n"
formatAvgChg = 0


#def printDashes:
#    print
# Define the path to the file to read
filePath = 'Resources/PyBankData.csv'


with open(filePath, 'r') as csvfile:
    data = csv.reader(csvfile) #Dump the entire file into the variable DATA
    next(data)  #skips the header line (Row 1 in Excel)
#   Loops through rows 2 to end of file
    for row in data:
        if row[0] == 'Jan-2010': #If we're in the first row set the previous row to current row (it's a hack)
            previousRow = int(row[1])
        totalEarnings = totalEarnings + int(row[1]) #start adding up earnings
        monthCount = monthCount +  1 #count the months
        monthlyDelta = int(row[1]) - previousRow #find the difference between months
        totalDelta = totalDelta  + monthlyDelta #running total of profit/loss
#         print(row[0]," ",row[1]," ",monthlyDelta) #print the original CSV + 3rd column with monthly change
#       Loop to check if the current monthlyDelta is bigger than current theBiggest
#       if it is, reassign the values in the BiggestMonth array to this row's
#       month and the current monthly delta. Repeat for smallest monthlyDelta
        if monthlyDelta > theBiggest:
            theBiggest = monthlyDelta
            biggestMonth[0] = row[0]
            biggestMonth[1] = theBiggest
        if monthlyDelta < theSmallest:
            theSmallest = monthlyDelta
            smallestMonth[0] = row[0]
            smallestMonth[1] = theSmallest
        previousRow = int(row[1]) # reassign previous row to current row
#    calculate the average change.  Have to subtract one month because there are only 85 items in this column

    averageChange = float(totalDelta)/float(monthCount-1)
    formatAvgChg = "{:.2f}".format(averageChange)
#    Print all your results

    print(title)
    print("Months in reporting period:    ", monthCount)
    print("Cumulative earnings:           $", totalEarnings)
    print(('Average Change:              $'+"{:.2f}").format(averageChange))
    print('Greatest increase in profits : ', biggestMonth[0], "$", biggestMonth[1])
    print("Greatest decrease in profits : ", smallestMonth[0], "$", smallestMonth[1])

txtFile = open(outputFile, 'w')
txtFile.write(title)
txtFile.write('Months in reporting period:     ')
txtFile.write(str(monthCount))
txtFile.write('\n')
txtFile.write('Cumulative earnings:            $')
txtFile.write(str(totalEarnings))
txtFile.write('\n')
txtFile.write('Average Change:                 $')
txtFile.write(str((formatAvgChg)))
txtFile.write('\n')
txtFile.write('Greatest increase in profits:    ')
txtFile.write(str(biggestMonth[0]))
txtFile.write('\t')
txtFile.write('$')
txtFile.write(str(biggestMonth[1]))
txtFile.write('\n')
txtFile.write('Greatest decrease in profits:     ')
txtFile.write(str(smallestMonth[0]))
txtFile.write('\t')
txtFile.write('$' )
txtFile.write(str(smallestMonth[1]))
txtFile.write('\n')
txtFile.close()
