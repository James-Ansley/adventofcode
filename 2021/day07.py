with open('input_files/day07') as f:
    data = [int(x) for x in f.read().split(',')]

linear_weights = [0] * len(data)
quadratic_weights = [0] * len(data)
for i in range(len(data)):
    for position in data:
        move = abs(position - i)
        linear_weights[i] += move
        quadratic_weights[i] += move * (move + 1) // 2

print(min(linear_weights))
print(min(quadratic_weights))
