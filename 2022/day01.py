with open("input_files/day01", "r") as f:
    data = f.read().split("\n\n")
    data = [[int(item) for item in pack.splitlines()] for pack in data]
    data = [sum(pack) for pack in data]
    data = sorted(data)

print(data[-1])
print(sum(data[-3:]))
