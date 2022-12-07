import re

with open("input_files/day07", "r") as f:
    data = iter(f.read().splitlines())

sizes = []
stack = [0]
while stack:
    line = next(data, None)
    if line is None or line == "$ cd ..":
        child = stack.pop()
        if stack:
            sizes.append(child)
            stack[-1] += child
    elif cd := re.match(r"\$ cd .+", line):
        stack.append(0)
    elif file := re.match(r"(\d+) .+", line):
        stack[-1] += int(file.group(1))

space_needed = 30_000_000 - (70_000_000 - sizes[-1])
sizes = sorted(sizes)

print(sum(elt for elt in sizes if elt <= 100_000))
print(next(elt for elt in sizes if elt >= space_needed))
