# -------
# Day 1
# -------

import csv

# allLines = []

# with open('day1.csv', newline='') as data:
#     reader = csv.DictReader(data)
#     for row in reader:
#         allLines.append(int(row['data'].strip()))
# allLines.sort()

# for i in range(10):
#     for j in range(len(allLines)):
#         if (allLines[i] + allLines[j]) == 2020:
#             print(allLines[i] * allLines[j])



# -------
# Day 2
# -------

# allLines = []
# count = 0

# with open('day2.csv', newline='') as data:
#     reader = csv.DictReader(data)
#     for row in reader:
#         allLines.append(row['data'].strip().replace('-', ' ').replace(':', ' ').split(' '))

# for line in allLines:
#     if int(line[0]) <= line[4].replace(line[2], '1').count('1') <= int(line[1]):
#         count+=1

# print(count)


# -------
# Day 3
# -------

allLines = []

with open('day3.csv', newline='') as data:
    reader = csv.DictReader(data)
    for row in reader:
        allLines.append(row['data'])
        print(row['data'])

