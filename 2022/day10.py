with open("input_files/day10", "r") as f:
    data = f.read().splitlines()
    data = [line.split() for line in reversed(data)]

clock = 0
x_reg = 1
strength = 0
pixels = []
while data:
    instr = data.pop()
    pixels += "#" if abs(clock % 40 - x_reg) <= 1 else " "
    clock += 1
    if (20 + clock) % 40 == 0:
        strength += clock * x_reg
    if instr[0] == "addx":
        data.append(("add", instr[1]))
    if instr[0] == "add":
        x_reg += int(instr[1])

print(strength)
print("\n".join(" ".join(pixels[i:i + 40]) for i in range(0, len(pixels), 40)))
