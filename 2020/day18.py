import re

with open('input_files/day18') as f:
    data = f.read().split('\n')
    data = [line.replace(' ', '') for line in data]


def evaluate1(expr):
    while '(' in expr:
        expr = re.sub(r'\(([^()]+)\)', lambda m: str(evaluate1(m.group(1))), expr)
    while '+' in expr or '*' in expr:
        expr = re.sub(r'^(\d+)\+(\d+)', lambda m: str(int(m.group(1)) + int(m.group(2))), expr)
        expr = re.sub(r'^(\d+)\*(\d+)', lambda m: str(int(m.group(1)) * int(m.group(2))), expr)
    return int(expr)


def evaluate2(expr):
    while '(' in expr:
        expr = re.sub(r'\(([^()]+)\)', lambda m: str(evaluate2(m.group(1))), expr)
    while '+' in expr:
        expr = re.sub(r'(\d+)\+(\d+)', lambda m: str(int(m.group(1)) + int(m.group(2))), expr)
    while '*' in expr:
        expr = re.sub(r'(\d+)\*(\d+)', lambda m: str(int(m.group(1)) * int(m.group(2))), expr)
    return int(expr)


total = sum(evaluate1(expr) for expr in data)
print(total)

total = sum(evaluate2(expr) for expr in data)
print(total)
