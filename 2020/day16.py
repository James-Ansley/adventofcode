import re
from math import prod

with open('input_files/day16') as f:
    rules, ticket, others = f.read().split('\n\n')

    rules = re.findall(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', rules)
    rules = [(n, *map(int, vals)) for n, *vals in rules]

    ticket = ticket.split('\n')[1].split(',')
    ticket = [int(x) for x in ticket]

    others = others.split('\n')[1:]
    others = [tuple(map(int, other.split(','))) for other in others]

valid_numbers = set()
valid_numbers.update(*(range(r[1], r[2] + 1) for r in rules))
valid_numbers.update(*(range(r[3], r[4] + 1) for r in rules))

total = 0
for other in others:
    total += sum(val for val in other if val not in valid_numbers)

print(total)

others = [other for other in others if all(val in valid_numbers for val in other)]

possible_rules = [set(rules) for _ in rules]
for other in others:
    for i, val in enumerate(other):
        possible_rules[i] = {r for r in possible_rules[i] if r[1] <= val <= r[2] or r[3] <= val <= r[4]}

rules = {}
while len(rules) < len(ticket):
    for i, possible_rule in enumerate(possible_rules):
        if len(possible_rule) == 1:
            rules[i] = possible_rule.pop()
            for other_rules in possible_rules:
                other_rules.discard(rules[i])

val = prod(ticket[i] for i, rule in rules.items() if 'departure' in rule[0])

print(val)
