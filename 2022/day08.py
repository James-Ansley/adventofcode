from math import prod

with open("input_files/day08", "r") as f:
    data = f.read().splitlines()

data = [[int(e) for e in line] for line in data]
data_t = [*zip(*data)]

invisibles = 0
best_scenic_score = 0
for i in range(1, len(data) - 1):
    row = data[i]
    for j in range(1, len(data[0]) - 1):
        col = data_t[j]
        target = data[i][j]
        runs = (row[j - 1::-1], row[j + 1:], col[i - 1::-1], col[i + 1:])

        invisibles += all(any(t >= target for t in run) for run in runs)
        score = prod(
            next((k + 1 for k, t in enumerate(run) if t >= target), len(run))
            for run in runs
        )
        best_scenic_score = max(best_scenic_score, score)

print(len(data[0]) * len(data) - invisibles)
print(best_scenic_score)
