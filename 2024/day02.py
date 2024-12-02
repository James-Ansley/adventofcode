from collections.abc import Iterator
from itertools import pairwise


def dampened(report: list[int]) -> Iterator[list[int]]:
    for i in range(len(report)):
        yield report[:i] + report[i + 1:]


def is_safe(report: list[int]) -> bool:
    differences = [e1 - e2 for e1, e2 in pairwise(report)]
    return (
        all(0 < d <= 3 for d in differences)
        or all(-3 <= d < 0 for d in differences)
    )


with open("input_files/day02", "r") as f:
    data = [[int(e) for e in line.split()] for line in f]

naive_safety = sum(is_safe(r) for r in data)
dampened_safety = sum(any(is_safe(r1) for r1 in dampened(r)) for r in data)

print(naive_safety)
print(dampened_safety)
