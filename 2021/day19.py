from itertools import combinations


class Scanner:
    rotation_lambdas = [
        lambda x, y, z: ((-y, x, z), (-x, -y, z), (y, -x, z)),  # x 90, 180, 270
        lambda x, y, z: ((z, y, -x), (-x, y, -z), (-z, y, x)),  # y 90, 180, 270
        lambda x, y, z: ((x, -z, y), (x, -y, -z), (x, z, -y)),  # z 90, 180, 270
    ]

    def __init__(self, points):
        self.points = frozenset(points)
        self.rotations = self.get_rotations()
        self.position = (0, 0, 0)

    def get_rotations(self):
        point_clouds = {self.points}
        for rot in Scanner.rotation_lambdas:
            temp_clouds = set()
            for cloud in point_clouds:
                rotated = set(zip(*(rot(*point) for point in cloud)))
                temp_clouds |= rotated
            point_clouds |= temp_clouds
        return point_clouds


def match(anchor, scanner):
    for rotation in scanner.rotations:
        for x1, y1, z1 in anchor.points:
            for x2, y2, z2 in rotation:
                dx, dy, dz = x1 - x2, y1 - y2, z1 - z2
                cloud = set((x + dx, y + dy, z + dz) for x, y, z in rotation)
                if len(anchor.points & cloud) >= 12:
                    return cloud, (dx, dy, dz)
    return None, None


with open('input_files/day19') as f:
    data = f.read().strip().split('\n\n')
    data = [line.split('\n')[1:] for line in data]
    data = [[line.split(',') for line in cloud] for cloud in data]
    data = [[tuple(int(x) for x in line) for line in cloud] for cloud in data]

scanners = [Scanner(cloud) for cloud in data]

points = {*data[0]}
to_match = scanners[1:]
anchors = [scanners[0]]
while anchors:
    anchor = anchors.pop()
    temp = []
    for scanner in to_match:
        abs_points, position = match(anchor, scanner)
        if abs_points is not None:
            points |= abs_points
            scanner.points = abs_points
            anchors.append(scanner)
            scanner.position = position
        else:
            temp.append(scanner)
    to_match = temp

print(len(points))

dist = 0
scanner_positions = {scanner.position for scanner in scanners}
for (x1, y1, z1), (x2, y2, z2) in combinations(scanner_positions, 2):
    dist = max(dist, abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2))
print(dist)
