from math import prod

with open('input_files/day13') as f:
    arrival, ids = f.read().split()
    arrival = int(arrival)
    ids = ids.split(',')
    times = [(int(x), -i) for i, x in enumerate(ids) if x != 'x']


dep = arrival
while True:
    if any(dep % (t := time) == 0 for time, _ in times):
        break
    dep += 1

print((dep - arrival) * t)


N = prod(time for time, _ in times)
time = 0
for m, bi in times:
    Ni = N // m
    xi = Ni ** (m - 2) % m
    time += bi * Ni * xi

print(time % N)
