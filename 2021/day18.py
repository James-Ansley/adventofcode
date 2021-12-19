import math
from collections import deque
from itertools import permutations


def explode(pair):
    stack = []
    depth, to_add, last_digit = 0, 0, None
    while pair:
        stack.append(pair.popleft())
        if stack[-1] == '[':
            if depth < 4:
                depth += 1
            else:
                left, right, _ = (pair.popleft() for _ in range(3))
                if last_digit is not None:
                    stack[last_digit] += left + to_add
                to_add = right
                stack[-1] = 0
                last_digit = len(stack) - 1
        elif stack[-1] == ']':
            depth -= 1
        elif isinstance(stack[-1], int):
            stack[-1] += to_add
            to_add = 0
            last_digit = len(stack) - 1
    return deque(stack)


def split(pair):
    new_pair = deque()
    while pair:
        char = pair.popleft()
        if isinstance(char, int) and char > 9:
            left, right = math.floor(char / 2), math.ceil(char / 2)
            new_pair.extend(('[', left, right, ']'))
            return new_pair + pair, True
        new_pair.append(char)
    return new_pair, False


def reduce(pair):
    has_split = True
    while has_split:
        pair = explode(pair)
        pair, has_split = split(pair)
    return pair


def magnitude(pair):
    stack = []
    for char in pair:
        if char == ']':
            right, left = stack.pop(), stack.pop()
            stack.append(left * 3 + right * 2)
        elif isinstance(char, int):
            stack.append(char)
    return stack[0]


with open('input_files/day18') as f:
    data = f.read().splitlines()
    data = [(c for c in line if c != ',') for line in data]
    data = [[int(c) if c.isdigit() else c for c in line] for line in data]

sum_ = data[0]
for pair in data[1:]:
    sum_ = deque(('[', *sum_, *pair, ']'))
    sum_ = reduce(sum_)
print(magnitude(sum_))

max_ = 0
for x, y in permutations(data, 2):
    sum_ = reduce(deque(('[', *x, *y, ']')))
    max_ = max(max_, magnitude(sum_))
print(max_)
