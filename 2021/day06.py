from collections import Counter


def run(n, fish):
    for _ in range(n):
        new_fish = {timer - 1: count for timer, count in fish.items()}
        new_fish.pop(-1, None)
        if 0 in fish:
            new_fish[8] = fish[0]
            new_fish[6] = fish[0] + new_fish.get(6, 0)
        fish = new_fish
    return sum(fish.values())


with open('input_files/day06') as f:
    fish_data = Counter(map(int, f.read().split(',')))

print(run(80, fish_data))
print(run(256, fish_data))
