import json
from functools import cmp_to_key


def compare(l, r):
    for l1, r1 in zip(l, r):
        if r1 == l1:
            continue
        if isinstance(l1, int) and isinstance(r1, int):
            return (l1 > r1) - (l1 < r1)
        l1 = [l1] if isinstance(l1, int) else l1
        r1 = [r1] if isinstance(r1, int) else r1
        if (res := compare(l1, r1)) != 0:
            return res
    return (len(l) > len(r)) - (len(l) < len(r))


with open("input_files/day13", "r") as f:
    data = f.read().split("\n\n")
    data = [line.split() for line in data]
    data = [[json.loads(val) for val in group] for group in data]

flat_data = [v for group in data for v in group]
flat_data += [[2]], [[6]], []
flat_data = sorted(flat_data, key=cmp_to_key(compare))

print(sum(i + 1 for i, v in enumerate(data) if compare(*v) == -1))
print(flat_data.index([[2]]) * flat_data.index([[6]]))
