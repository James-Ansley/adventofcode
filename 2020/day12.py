import re

with open('input_files/day12') as f:
    data = re.findall(r'(\w)(\d+)', f.read())
    data = [(instr, int(val)) for instr, val in data]

angle = 0
angles = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}
pos = {'E': 0, 'N': 0, 'W': 0, 'S': 0}
for instr, val in data:
    if instr == 'R':
        val = -val
    if instr in 'LR':
        angle = (angle + val) % 360
    else:
        if instr == 'F':
            instr = angles[angle]
        pos[instr] += val

print(abs(pos['E'] - pos['W']) + abs(pos['N'] - pos['S']))

x, y = 0, 0
wx, wy = 10, 1
deltas = {'E': (1, 0), 'N': (0, 1), 'W': (-1, 0), 'S': (0, -1)}
sin = {0: 0, 90: 1, 180: 0, 270: -1, 360: 0}
for instr, val in data:
    if instr == 'R':
        val = (-val) % 360
    if instr in 'LR':
        s, c = sin[val], sin[val + 90]
        wx, wy = round(wx * c - wy * s), round(wx * s + wy * c)
    elif instr == 'F':
        x, y = x + wx * val, y + wy * val
    else:
        xd, yd = deltas[instr]
        wx, wy = wx + xd * val, wy + yd * val

print(abs(x) + abs(y))
