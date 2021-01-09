with open('../input_files/day25') as f:
    card, door = f.read().split('\n')
    card, door = int(card), int(door)

door_loop = 0
value = 1
while value != door:
    value = (value * 7) % 20201227
    door_loop += 1

print(pow(card, door_loop, 20201227))
