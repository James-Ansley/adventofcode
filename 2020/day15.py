from collections import defaultdict

with open('input_files/day15') as f:
    data = f.read().split(',')
    data = [int(x) for x in data]


def run(finish):
    numbers = defaultdict(list)
    numbers |= {data[i]: [i + 1] for i in range(len(data))}

    last = data[-1]
    for i in range(len(data) + 1, finish + 1):
        if len(numbers[last]) > 1:
            last = numbers[last][-1] - numbers[last][-2]
        else:
            last = 0
        numbers[last].append(i)
    return last


print(run(2020))
print(run(30000000))
