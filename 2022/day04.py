import re

with open("input_files/day04", "r") as f:
    data = re.findall(r"(\d+)-(\d+),(\d+)-(\d+)", f.read())
    data = [[int(e) for e in row] for row in data]

contained = [(a <= c <= d <= b or c <= a <= b <= d) for a, b, c, d in data]
overlap = [max(a, c) <= min(b, d) for a, b, c, d in data]

print(sum(contained))
print(sum(overlap))
