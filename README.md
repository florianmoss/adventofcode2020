# Advent of Code 2020

Chosen language: `Python3`. The structure is pretty self explainatory - all code is in `solution.py`. The files containing the data are named appropiately.

## Day 1
The simplest solution would be to loop over a list and see if the 2 added values add up to 2020. For (b), the same could be done with 3 loops.

The `itertools` module provides a function called `combinations` that spits out an iterable list of all combinations of the order `n` (here 2 and 3). The only other step is, finding the combination that ends up with the sum `2020`. I chose to make use of the `filter` function, which takes in a function and an iterable. Each combination is being tested for the sum 2020, if found the result is returned.

## Day 2
Solution for (a) is pretty basic, iterate over item and check that the `letter` in question appears at `min` and `max`. (b) asked to check for the letter in question to be present at exactly one position. It would have been better to use a regular expression - but I already had the loop going on, so I threw in a couple of conditions:
1. Make sure that the string is longer than the min and max position
2. Check that the letter is available at one of the positions but not both. 

## Day 3
How many `#` are hit while iterating the input. I simply loop over it and define the steps for `down` and `sideways`. Simply check when the right boarder is hit and reset to the left and count the `#`s along the way.

## Day 4
Practicing regular expressions! Just to annoy Murph, I chose to use 2 loops for (a). The loops are just checking if all the required attributes are present in each line. I also removed all missing entries from the list, the list size is the solution.

With the clean data at hand, the only thing to do is to iterate over it and check all the conditions. I created a dictionary (hashmap) for each entry and then used regular expressions and simple integer comparisons to find correct entries.

## Day 5 
Straight forward -  the first 7 values had to be converted to a base 10 integer, same for the last 3 values. Once sorted, the last value is the solution for (a). The solution for (b) is simply the missing seat. Iterate over the entries and check for a gap. Since n and n+1 are always uneven, I simply used this to look for modulo-2 == 0. 