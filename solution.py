# -------
# Day 1
# -------

import csv

allLines = []

with open('day1.csv', newline='') as data:
    reader = csv.DictReader(data)
    for row in reader:
        allLines.append(int(row['data'].strip()))
allLines.sort()

for i in range(10):
    for j in range(len(allLines)):
        if (allLines[i] + allLines[j]) == 2020:
            print("Day 1: {0}".format(allLines[i] * allLines[j]))



# -------
# Day 2
# -------

allLines = []
count = 0

with open('day2.csv', newline='') as data:
    reader = csv.DictReader(data)
    for row in reader:
        allLines.append(row['data'].strip().replace('-', ' ').replace(':', ' ').split(' '))

for line in allLines:
    if int(line[0]) <= line[4].replace(line[2], '1').count('1') <= int(line[1]):
        count+=1

print("Day 2: {0}".format(count))


# -------
# Day 3
# -------


arr = []

with open('day3.csv', newline='') as data:
    reader = csv.DictReader(data)
    for row in reader:
        arr.append(row['data'])

pos = 0
count = 0

for x in arr:
    if x[pos]=='#':
        count += 1
   
    if pos<28:
        pos += 3
    elif pos==28:
        pos = 0
    elif pos==29:
        pos = 1
    else:
        pos = 2

print("Day 3: {0}".format(count))

