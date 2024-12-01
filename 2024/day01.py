from collections import Counter

with open("input_files/day01", "r") as f:
    data = [line.strip().split() for line in f]

list1 = sorted(int(e[0]) for e in data)
list2 = sorted(int(e[1]) for e in data)
list2_freq = Counter(list2)

differences = sum(abs(e0 - e1) for e0, e1 in zip(list1, list2))
similarity = sum(e * list2_freq[e] for e in list1)

print(differences)
print(similarity)
