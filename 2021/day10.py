from bisect import insort


def get_mismatches(line):
    brackets = {'(': ')', '[': ']', '<': '>', '{': '}'}
    stack = []
    for i in range(len(line)):
        if line[i] in brackets:
            stack.append(i)
        if line[i] in brackets.values():
            open_index = stack.pop()
            if brackets[line[open_index]] != line[i]:
                return [line[i]]
    return [brackets[line[i]] for i in reversed(stack)]


with open('input_files/day10') as f:
    data = [line for line in f]

weights = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

order = [None, ')', ']', '}', '>']

mismatch_score = 0
scores = []
for line in data:
    mismatches = get_mismatches(line)
    if len(mismatches) == 1:
        mismatch_score += weights[mismatches[0]]
    else:
        partial = 0
        for bracket in mismatches:
            partial = partial * 5 + order.index(bracket)
        insort(scores, partial)

print(mismatch_score)
print(scores[len(scores) // 2])
