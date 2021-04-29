#!/usr/bin/env python3

from csv import writer as csvWriter
from sys import argv

###

# Parse first argument to get number of rolls to simulate
try:
  numberOfRolls = int(argv[1])
except:
  # Default number of rolls
  numberOfRolls = 100

###

# Number of ways to get each point total
points = {}
# Total points it is possible to have on each roll
rolls = {}

#

def performRolls(lastRolls):
  thisRoll = {} # What values can we get?
  for roll in range(2, 7): # Possible rolls
    for oldTotal in lastRolls:
      newTotal = oldTotal + roll # What total are we up to now?
      # How many ways did we know about for getting this total? We have one more
      thisRoll[newTotal] = thisRoll.get(newTotal, lastRolls.get(newTotal, 0)) + 1
  return thisRoll


def calculateRolls(stop):
  lastRoll = {0: 0} # To start us off, we have a total of zero after zero rolls
  for rollCounter in range(stop):
    # Pass the results of each roll to the next roll
    lastRoll = rolls[rollCounter + 1] = performRolls(lastRoll)
    # Record the points the most recent roll reached
    for pointsScored in lastRoll:
        points[pointsScored] = lastRoll[pointsScored]

calculateRolls(numberOfRolls)

#

def writeRollBreakdownToCsv():
  maxRollTotal = max(points) # Should be 6 * numberOfRolls!
  with open(f'breakdown-after-{numberOfRolls}-rolls.csv', 'w') as csvFile:
    csv = csvWriter(csvFile)
    csv.writerow(['Roll #'] + [f'Ways to roll {total + 1}' for total in range(1, maxRollTotal)])
    for num, possibleTotals in sorted(rolls.items()):
      # Create an empty row, then fill in the totals
      row = [num] + [''] * (maxRollTotal - 1)
      for total, count in possibleTotals.items():
          row[total - 1] = count
      csv.writerow(row)

writeRollBreakdownToCsv()

#

def writePointsToCsv():
  with open(f'points-up-to-{numberOfRolls}-rolls.csv', 'w') as csvFile:
    csv = csvWriter(csvFile)
    csv.writerow(['Point Value', 'Number of Ways to Roll'])
    csv.writerows(sorted(points.items()))

writePointsToCsv()
