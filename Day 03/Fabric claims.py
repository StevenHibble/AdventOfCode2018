import os

os.chdir('Day 03')

### Setup
with open('Input.txt', 'r') as f:
    data = f.read().splitlines()

class elfClaim:
    """A class to hold each Elf's claim"""

    def __init__(self, instruction):
        inst = instruction.replace('#', '').replace(' @', '').replace(',', ' ').replace(':', '').replace('x', ' ')
        inst = list(map(int, inst.split(' ')))

        self.instruction = instruction
        self.id = inst[0]
        self.x_offset = inst[1]
        self.y_offset = inst[2]
        self.x_len = inst[3]
        self.y_len = inst[4]

    def __repr__(self):
        return self.instruction

    def __str__(self):
        return self.instruction

    def get_corners(self):
        return [{'x': self.x_offset,                  'y': self.y_offset}, 
                {'x': self.x_offset + self.x_len - 1, 'y': self.y_offset}, 
                {'x': self.x_offset + self.x_len - 1, 'y': self.y_offset + self.y_len - 1}, 
                {'x': self.x_offset,                  'y': self.y_offset + self.y_len - 1}]

claims = list(map(elfClaim, data))


### Part One
fabric = [[0] * 1000 for i in range(1000)]

