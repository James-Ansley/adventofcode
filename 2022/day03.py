from string import ascii_letters

with open("input_files/day03", "r") as f:
    data = f.read().splitlines()

middles = [len(line) // 2 for line in data]
compartments = [(line[:i], line[i:]) for line, i in zip(data, middles)]
compartments = [(set(c1) & set(c2)).pop() for c1, c2 in compartments]

groups = [data[i: i + 3] for i in range(0, len(data), 3)]
groups = [map(set, group) for group in groups]
groups = [set.intersection(*group).pop() for group in groups]

print(sum(ascii_letters.index(item) + 1 for item in compartments))
print(sum(ascii_letters.index(item) + 1 for item in groups))
