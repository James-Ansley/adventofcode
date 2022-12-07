import re
from dataclasses import dataclass, field
from itertools import chain, repeat


@dataclass
class Directory:
    size: int
    children: list["Directory"] = field(default_factory=list)


with open("input_files/day07", "r") as f:
    data = f.read().splitlines()

data = chain(data, repeat("$ cd .."))

sizes = []
stack = [Directory(0)]
while stack:
    line = next(data)
    if line == "$ cd ..":
        child = stack.pop()
        if stack:
            sizes.append(child.size)
            stack[-1].size += child.size
    elif cd := re.match(r"\$ cd (.+)", line):
        directory = Directory(0)
        stack[-1].children.append(directory)
        stack.append(directory)
    elif file := re.match(r"(\d+) .+", line):
        stack[-1].size += int(file.group(1))

space_needed = 30_000_000 - (70_000_000 - sizes[-1])
sizes = sorted(sizes)

print(sum(elt for elt in sizes if elt <= 100_000))
print(next(elt for elt in sizes if elt >= space_needed))
