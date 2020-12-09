import re


with open('../input_files/day2') as f:
    data = re.findall(r'(\d+)-(\d+) (\w): (\w+)', f.read())
    data = [(int(fr), int(to), c, word) for fr, to, c, word in data]

print(sum(fr <= word.count(c) <= to for fr, to, c, word in data))

print(sum((word[fr-1] == c) != (word[to - 1] == c) for fr, to, c, word in data))
