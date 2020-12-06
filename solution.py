# Variables and Imports

# SESSIONID= '<session_from_browser>'
import csv
import re
import requests
from itertools import *

# -------
# Day 1
# -------

allLines = []

with open('day1.csv', newline='') as data:
    reader = csv.DictReader(data)
    for row in reader:
        allLines.append(int(row['data'].strip()))

all_combinations_a = list(combinations(allLines, 2))
all_combinations_b = list(combinations(allLines, 3))

def sums_to_2020(values):
    return sum(values) == 2020

result_a = list(filter(sums_to_2020, all_combinations_a))
result_b = list(filter(sums_to_2020, all_combinations_b))

print("Day 1 (a): {0}".format(result_a))
print("Day 1 (b): {0}".format(result_b))


# -------
# Day 2
# -------

allLines = []

count = 0
count_2 = 0

with open('day2.csv', newline='') as data:
    reader = csv.DictReader(data)
    for row in reader:
        allLines.append(row['data'].strip().replace('-', ' ').replace(':', ' ').split(' '))

for line in allLines:
    if int(line[0]) <= line[4].count(line[2]) <= int(line[1]):
        count+=1
    low = int(line[0])
    high = int(line[1])
    if high <= len(line[4]) and low <= len(line[4]):
        if (line[4][low-1] == line[2] or line[4][high-1] == line[2]) \
            and not (line[4][low-1] == line[2] \
                and line[4][high-1] == line[2]):
            count_2+=1



print("Day 2 (a): {0}".format(count))
print("Day 2 (b): {0}".format(count_2))


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


# -------
# Day 4
# -------

# r = requests.get('https://adventofcode.com/2020/day/4/input', cookies={'session': SESSIONID})
# f= open("day4.txt","w")
# f.write(r.text)

attr = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
data = open('day4.txt').read().replace('\n', ' ').split('  ')

for item in data[:]:
    for substr in attr:
        if substr not in item: 
            data.remove(item)  # this is done for part (b), it removes bad entries
            break
           
print("Day 4 (a): {0}".format(len(data)))


count = 0
pattern_pid = '^[0-9]{9}$'
pattern_hcl = '^#[0-9,a-f]{6}$'

for item in data:
    item = re.sub("\s+", ",", item.strip())
    converted_data = (dict(u.split(":") for u in item.split(",")))

    if ((converted_data['hgt'][-1] == 'm' and (150 <= int(converted_data['hgt'][:-2]) <= 193)) or \
        (converted_data['hgt'][-1] == 'n' and (59 <= int(converted_data['hgt'][:-2]) <= 76))) and \
        1920 <= int(converted_data['byr']) <= 2002 and \
        2010 <= int(converted_data['iyr']) <= 2020 and \
        2020 <= int(converted_data['eyr']) <= 2030 and \
        converted_data['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
        re.match(pattern_pid, converted_data['pid']) and \
        re.match(pattern_hcl, converted_data['hcl']):
                count += 1

print("Day 4 (b): {0}".format(count))


# -------
# Day 5
# -------

arr = []

with open('day5.csv', newline='') as data:
    reader = csv.DictReader(data)
    for row in reader:
        arr.append(row['data'].replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"))

arr.sort()
print("Day 5 (a): The last value: {0}-{1}".format(int(arr[len(arr)-1][:7], 2), int(arr[len(arr)-1][7:], 2)))

last_val = int(arr[1][7:], 2)
for i in arr:
    if (int(i[7:], 2) + last_val) % 2 == 1:
        last_val = int(i[7:], 2)
    else:
        print("Day 5 (b): The value before : {0}-{1}".format(int(i[:7], 2), int(i[7:], 2)))
        break