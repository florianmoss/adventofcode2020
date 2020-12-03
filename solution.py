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
            print("Day 1 (a): {0}".format(allLines[i] * allLines[j]))

def day1_a():
    for i in range(10):
        for j in range(len(allLines)):
            for k in range(len(allLines)):
                if (allLines[i] + allLines[j] + allLines[k]) == 2020:
                    return allLines[i] * allLines[j] * allLines[k]

print("Day 1 (b): {0}".format(day1_a()))

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


def day3_solver(right, down):
    pos = 0
    count = 0
    for x in range(0, len(arr), down):
        if arr[x][pos]=='#':
            count += 1
   
        if pos<len(arr[x])-right:
            pos += right
        else:
            pos -= (len(arr[x])-right)
    return count

one = day3_solver(1, 1)
three = day3_solver(3, 1)
five = day3_solver(5, 1)
seven = day3_solver(7, 1)
one_2 = day3_solver(1, 2)

print("Day 3 (a): {0}".format(day3_solver(3, 1)))
print("Day 3 (b): {0}".format(one*three*five*seven*one_2))

