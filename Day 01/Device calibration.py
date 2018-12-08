import os

# Change to the first day directory
os.chdir('Day 01')

### Setup
# Read file
# NOTE: Using with closes the file (even when there's an error), keeping memory usage lower
with open('Input.txt', 'r') as file:
    data = file.read().splitlines()

# List comprehension to replace on each element
data = [value.replace('+', '') for value in data]

# python 3 requires map to be explicitly cast back into a list
data = list(map(int, data))

### Part 1
# f-string to interpolate
print(f'The answer to part 1 is: {sum(data)}')

### Part 2
from itertools import cycle

freqs = {0} # This is a set. A list ("[0]") took 200x longer
currentFreq = 0

for i, val in enumerate(cycle(data)):
    currentFreq += val

    if currentFreq in freqs:
        print(f'The answer to part 2 is: {currentFreq} (this took {i} iterations)')
        break

    freqs.add(currentFreq)

# A more pythonic solution (taken from Reddit: https://www.reddit.com/r/adventofcode/comments/a20646/2018_day_1_solutions/eauapmb/):
from itertools import accumulate

freqs = {0}

# accumulate takes cumulative sums
# next pulls the next value from an iterator
print(next(f for f in accumulate(cycle(data)) if f in freqs or freqs.add(f)))