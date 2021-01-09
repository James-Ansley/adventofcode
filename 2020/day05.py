import re


with open('input_files/day05') as f:
    data = f.read()
    data = re.sub(r'[FL]', '0', data)
    data = re.sub(r'[BR]', '1', data)
    data = data.split()
    data = {int(x, 2) for x in data}

print(m := max(data))

print(next(x for x in range(m) if x not in data and x - 1 in data))
