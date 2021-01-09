import re


def run():
    accumulator = 0
    visited = set()
    i = 0
    while i not in visited and i < len(data):
        visited.add(i)
        instr, val = data[i]
        if instr == 'acc':
            accumulator += val
        if instr == 'jmp':
            i += val - 1
        i += 1
    return accumulator, i >= len(data)


with open('input_files/day08') as f:
    data = re.findall(r'(.+?) ([+-]\d+)', f.read())
    data = [(instr, int(val)) for instr, val in data]

print(run()[0])

for i in (idx for idx in range(len(data)) if data[idx][0] in ('nop', 'jmp')):
    instr, val = data[i]
    data[i] = 'nop' if instr == 'jmp' else 'jmp', val

    acc, finished = run()
    if finished:
        print(acc)
        break

    data[i] = instr, val
