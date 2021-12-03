with open('input_files/day03') as f:
    data = [int(x, 2) for x in f]
    bits = max(x.bit_length() for x in data)

gamma = 0
for i in range(bits):
    gamma_bit = int(sum((x >> i) & 1 for x in data) > len(data) // 2)
    gamma |= gamma_bit << i

print(gamma * (2 ** bits - 1 ^ gamma))

o2, co2 = [*data], [*data]
for i in range(bits - 1, -1, -1):
    o2_bit = sum((x >> i) & 1 for x in o2) >= len(o2) / 2
    o2 = [x for x in o2 if (x >> i) & 1 == o2_bit]
    if len(o2) == 1:
        break

for i in range(bits - 1, -1, -1):
    co2_bit = sum((x >> i) & 1 for x in co2) < len(co2) / 2
    co2 = [x for x in co2 if (x >> i) & 1 == co2_bit]
    if len(co2) == 1:
        break

print(o2[0] * co2[0])
