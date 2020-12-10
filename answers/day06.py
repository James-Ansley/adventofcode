from functools import reduce


with open('../input_files/day06') as f:
    data = f.read().split('\n\n')

print(sum(len(set(group.replace('\n', ''))) for group in data))

count = 0
for group in data:
    answers = (set(ans) for ans in group.split())
    count += len(reduce((lambda x, y: x & y), answers))
print(count)
