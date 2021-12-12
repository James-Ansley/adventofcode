import re
from collections import defaultdict


def dfs(last, seen, edges, repeats):
    if last == 'end':
        return 1
    paths = 0
    for edge in edges[last]:
        if not (edge.islower() and edge in seen):
            paths += dfs(edge, seen | {edge}, edges, repeats)
        elif edge.islower() and edge in seen and repeats:
            paths += dfs(edge, seen, edges, False)
    return paths


with open('input_files/day12') as f:
    data = re.findall(r'(.*)-(.*)\n', f.read())

edges = defaultdict(list)
for v1, v2 in data:
    if v2 != 'start':
        edges[v1].append(v2)
    if v1 != 'start':
        edges[v2].append(v1)

print(dfs('start', set(), edges, False))
print(dfs('start', set(), edges, True))
