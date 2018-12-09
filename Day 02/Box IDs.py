import os

os.chdir('Day 02')

### Setup
with open('Input.txt', 'r') as f:
    data = f.read().splitlines()

### Part One: Count strings with exactly 2 or 3 of any letter
from itertools import chain


# For each character in a string, return the count if the count is 2 or 3
def find_twos_and_threes(input_string):
    return list(set([input_string.count(char) for char in input_string if input_string.count(char) in [2, 3]]))

# Combine everything into a single list
# chain.from_iterable unnests lists
tally_counts = list(map(find_twos_and_threes, data))
tally_counts = list(chain.from_iterable(tally_counts))

print(f'The answer to Part 1 is: {tally_counts.count(2) * tally_counts.count(3)}')


### Part Two: Find two similar strings
