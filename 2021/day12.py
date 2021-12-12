import re
from collections import defaultdict


def dfs(path, edges):
    if path[-1] == 'end':
        return 1
    paths = 0
    for edge in edges[path[-1]]:
        if not (edge.islower() and edge in path):
            paths += dfs(path + (edge,), edges)
    return paths


def dfs_repeats(path, edges):
    if path[-1] == 'end':
        return 1
    paths = 0
    for edge in edges[path[-1]]:
        has_double = any(path.count(v) == 2 for v in path if v.islower())
        if not (edge.islower() and edge in path and has_double):
            paths += dfs_repeats(path + (edge,), edges)
    return paths


with open('input_files/day12') as f:
    data = re.findall(r'(.*)-(.*)\n', f.read())

edges = defaultdict(list)
for v1, v2 in data:
    if v2 != 'start':
        edges[v1].append(v2)
    if v1 != 'start':
        edges[v2].append(v1)

print(dfs(('start',), edges))
print(dfs_repeats(('start',), edges))
