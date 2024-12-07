import re
from operator import add, mul


def run(equations, ops):
    result = 0
    for equation in equations:
        target, first, *rest = equation
        queue = [first]
        for value in rest:
            values = []
            for total in queue:
                for op in ops:
                    values.append(op(total, value))
            queue = values
        if target in queue:
            result += target
    return result


with open("input_files/day07", "r") as f:
    data = [re.split(r":? ", line.strip()) for line in f]
    data = [[int(e) for e in line] for line in data]

concat = lambda e1, e2: int(str(e1) + str(e2))

print(run(data, (add, mul)))
print(run(data, (add, mul, concat)))
