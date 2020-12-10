import re
from collections import defaultdict


with open('../input_files/day07') as f:
    data = f.read().split('\n')

forward_edges = {}
backward_edges = defaultdict(set)
for line in data:
    colour = re.match(r'(.+) bags contain', line).group(1)
    containees = re.findall(r'(\d+) (.+?) bag', line)
    containees = [(int(x), word) for x, word in containees]

    forward_edges[colour] = containees
    for _, containee in containees:
        backward_edges[containee].add(colour)

gold_bags = set()
bags = set(backward_edges['shiny gold'])
while bags:
    bag = bags.pop()
    gold_bags.add(bag)
    bags |= backward_edges[bag]
print(len(gold_bags))

n_bags = 0
bags = list(forward_edges['shiny gold'])
while bags:
    bag = bags.pop()
    n_bags += bag[0]
    bags += [(bag[0] * x, colour) for x, colour in forward_edges[bag[1]]]
print(n_bags)
