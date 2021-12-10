from bisect import insort


def get_mismatches(line):
    brackets = {'(': ')', '[': ']', '<': '>', '{': '}'}
    stack = []
    for i, char in enumerate(line):
        if char in brackets:
            stack.append(i)
        if char in brackets.values():
            if brackets[line[stack.pop()]] != char:
                return [char]
    return [brackets[line[i]] for i in reversed(stack)]


with open('input_files/day10') as f:
    data = list(f)

mismatch_weights = {')': 3, ']': 57, '}': 1197, '>': 25137}
closing_weights = {')': 1, ']': 2, '}': 3, '>': 4}

mismatch_score = 0
scores = []
for line in data:
    mismatches = get_mismatches(line)
    if len(mismatches) == 1:
        mismatch_score += mismatch_weights[mismatches[0]]
    else:
        partial = 0
        for bracket in mismatches:
            partial = partial * 5 + closing_weights[bracket]
        insort(scores, partial)

print(mismatch_score)
print(scores[len(scores) // 2])
