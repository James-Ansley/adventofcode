from collections import Counter
from operator import sub


with open('../input_files/day10') as f:
    data = [0] + sorted(int(x) for x in f)
    data.append(data[-1] + 3)

diffs = list(map(sub, data[1:], data))
count = Counter(diffs)
print(count[1] * count[3])

paths = [0] * (len(data) - 1) + [1]
for i in range(len(data) - 2, -1, -1):
    for j in range(i + 1, i + 4):
        if j < len(data) and data[j] - 3 <= data[i]:
            paths[i] += paths[j]
print(paths[0])
