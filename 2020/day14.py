import re

with open('input_files/day14') as f:
    data = re.findall(r'(.+) = (.+)', f.read())

mask0s = 0
mask1s = 0
mem = {}
for instr, val in data:
    if instr == 'mask':
        mask0s = int(val.replace('X', '1'), 2)
        mask1s = int(val.replace('X', '0'), 2)
    else:
        loc = instr[4:-1]
        mem[loc] = int(val) & mask0s | mask1s

print(sum(mem.values()))

mask = ''
mem = {}
for instr, val in data:
    if instr == 'mask':
        mask1s = int(val.replace('X', '0'), 2)
        mask = val
    else:
        loc = int(instr[4:-1])
        locs = [loc | mask1s]
        idxs = (idx for idx, x in enumerate(reversed(mask)) if x == 'X')
        for i in idxs:
            temp_locs = [loc & ~(1 << i) for loc in locs]
            temp_locs += [loc | (1 << i) for loc in locs]
            locs = temp_locs
        mem |= {loc: int(val) for loc in locs}

print(sum(mem.values()))
