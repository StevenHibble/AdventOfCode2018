import os

os.chdir('Day 03')

### Setup
with open('Input.txt', 'r') as f:
    data = f.read().splitlines()

class elfClaim:
    """A class to hold each Elf's claim"""

    def __init__(self, instructions):
        inst = instructions.replace('#', '').replace(' @', '').replace(',', ' ').replace(':', '').replace('x', ' ')
        inst = list(map(int, inst.split(' ')))

        self.instructions = instructions
        self.id = inst[0]
        self.dims = {'x': range(inst[1], inst[1] + inst[3]), # Range isn't inclusive for the end
                     'y': range(inst[2], inst[2] + inst[4])}

    def __repr__(self):
        return self.instructions

    def __str__(self):
        return self.instructions

    def overlap(self, other):
        x_overlap = set(self.dims['x']).intersection(other.dims['x'])
        y_overlap = set(self.dims['y']).intersection(other.dims['y'])

        if x_overlap and y_overlap:
            return {'x': range(min(x_overlap), max(x_overlap)+1),
                    'y': range(min(y_overlap), max(y_overlap)+1)}


claims = list(map(elfClaim, data))

### Part One
from itertools import combinations, product, chain

#tests = [elfClaim('#1 @ 1,3: 4x4'), elfClaim('#2 @ 3,1: 4x4'), elfClaim('#3 @ 5,5: 2x2')]
overlaps = []
for c1, c2 in combinations(claims, 2):
    o = c1.overlap(c2)

    if o is not None:
        print(f'{c1.id} :: {c2.id}: {o}')
        overlaps.append(o)

def expandOverlapToCoords(overlap):
    x = list(overlap['x'])
    y = list(overlap['y'])
    return list(product(x, y))

print(len(set(chain.from_iterable(map(expandOverlapToCoords, overlaps)))))
#print(set(chain.from_iterable(map(expandOverlapToCoords, overlaps))))
