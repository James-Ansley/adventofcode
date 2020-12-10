with open('../input_files/day01') as f:
    data = {int(x) for x in f}

for x in data:
    if 2020 - x in data:
        print(x * (2020 - x))
        break

list_data = list(data)
for i in range(len(data) - 2):
    for j in range(len(data) - 1):
        if 2020 - list_data[i] - list_data[j] in data:
            print(list_data[i] * list_data[j] * (2020 - list_data[i] - list_data[j]))
            break
    else:
        continue
    break
