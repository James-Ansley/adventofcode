with open('input_files/day09') as f:
    data = [int(x) for x in f]

for i in range(25, len(data)):
    nums = set(data[i-25: i])
    if all(data[i] - x not in nums for x in nums):
        print(data[i])
        break

idx = i
for i in range(idx):
    for j in range(i+2, idx):
        values = data[i:j]
        if sum(values) == data[idx]:
            print(min(values) + max(values))
            break
    else:
        continue
    break
