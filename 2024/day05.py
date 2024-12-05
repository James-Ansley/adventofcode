from collections import defaultdict
from functools import cmp_to_key
from itertools import combinations

with open("input_files/day05", "r") as f:
    rule_data, update_data = f.read().split("\n\n")
    update_data = update_data.splitlines()
    rule_data = rule_data.splitlines()

updates = [[int(e) for e in line.split(",")] for line in update_data]

rules = defaultdict(set)
for rule in rule_data:
    pre, post = rule.split("|")
    rules[int(pre)].add(int(post))

rule_key = cmp_to_key(lambda l, r: -1 if r in rules[l] else 1)

correct_total = 0
incorrect_total = 0
for update in updates:
    mid = len(update) // 2
    if all(r in rules[l] for l, r in combinations(update, 2)):
        correct_total += update[mid]
    else:
        incorrect_total += sorted(update, key=rule_key)[mid]

print(correct_total)
print(incorrect_total)
