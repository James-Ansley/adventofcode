from itertools import combinations

rotation_lambdas = [
    [lambda x, y, z: (-y, x, z),  # X
     lambda x, y, z: (-x, -y, z),
     lambda x, y, z: (y, -x, z)],
    [lambda x, y, z: (z, y, -x),  # Y
     lambda x, y, z: (-x, y, -z),
     lambda x, y, z: (-z, y, x)],
    [lambda x, y, z: (x, -z, y),  # Z
     lambda x, y, z: (x, -y, -z),
     lambda x, y, z: (x, z, -y)]
]


def get_rotations(points):
    point_clouds = {points}
    for rot90, rot180, rot_neg90 in rotation_lambdas:
        temp_clouds = set()
        for cloud in point_clouds:
            temp_clouds.add(frozenset(rot90(x, y, z) for x, y, z in cloud))
            temp_clouds.add(frozenset(rot180(x, y, z) for x, y, z in cloud))
            temp_clouds.add(frozenset(rot_neg90(x, y, z) for x, y, z in cloud))
        point_clouds |= temp_clouds
    return point_clouds


def match(anchor, rotations):
    for rotation in rotations:
        for x1, y1, z1 in anchor:
            for x2, y2, z2 in rotation:
                dx, dy, dz = x1 - x2, y1 - y2, z1 - z2
                cloud = set((x + dx, y + dy, z + dz) for x, y, z in rotation)
                if len(anchor & cloud) >= 12:
                    return cloud, (dx, dy, dz)
    return None, None


with open('input_files/day19') as f:
    data = f.read().strip().split('\n\n')
    data = [line.split('\n')[1:] for line in data]
    data = [[line.split(',') for line in cloud] for cloud in data]
    data = [[tuple(int(x) for x in line) for line in cloud] for cloud in data]
    data = [frozenset(cloud) for cloud in data]

points = {*data[0]}
abs_scanners = set()
scanners = [get_rotations(cloud) for cloud in data[1:]]
anchors = [data[0]]
while anchors:
    anchor = anchors.pop()
    to_match = []
    for clouds in scanners:
        abs_points, position = match(anchor, clouds)
        if abs_points is not None:
            points |= abs_points
            anchors.append(abs_points)
            abs_scanners.add(position)
        else:
            to_match.append(clouds)
    scanners = to_match

print(len(points))

dist = 0
for (x1, y1, z1), (x2, y2, z2) in combinations(abs_scanners, 2):
    dist = max(dist, abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2))
print(dist)
