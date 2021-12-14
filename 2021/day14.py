import re
from collections import Counter, defaultdict


def run(n, template, rules):
    chars = defaultdict(int, Counter(template))
    template = Counter(zip(template, template[1:]))
    for _ in range(n):
        temp = defaultdict(int)
        for pair, count in template.items():
            chars[rules[pair]] += count
            temp[pair[0], rules[pair]] += count
            temp[rules[pair], pair[1]] += count
        template = temp
    return max(chars.values()) - min(chars.values())


with open('input_files/day14') as f:
    template, rules = f.read().split('\n\n')

rules = re.findall(r'(\w+) -> (\w+)', rules)
rules = {tuple(pair): value for pair, value in rules}

print(run(10, template, rules))
print(run(40, template, rules))
