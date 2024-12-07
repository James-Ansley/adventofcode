import re
from operator import add, mul


def run(equations, ops):
    result = 0
    for target, first, *rest in equations:
        queue = [first]
        for value in rest:
            queue = [
                op(total, value)
                for total in queue
                for op in ops
                if total <= target
            ]
        if target in queue:
            result += target
    return result


def concat(a, b):
    i = 10
    while i <= b:
        i *= 10
    return a * i + b


with open("input_files/day07", "r") as f:
    data = [re.findall(r"(\d+)", line) for line in f]
    data = [[int(e) for e in line] for line in data]

print(run(data, (add, mul)))
print(run(data, (add, mul, concat)))
