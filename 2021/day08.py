import re

with open('input_files/day08') as f:
    data = re.findall(r'(.*) \| (.*)', f.read())
    data = [(inputs.split(), outputs.split()) for inputs, outputs in data]
    ins, outs = list(zip(*data))

uniques = 0
for outputs in outs:
    uniques += sum(len(output) in (2, 3, 4, 7) for output in outputs)

print(uniques)

output_sums = 0
for inputs, outputs in zip(ins, outs):
    digits = [set()] * 10
    digits[1] = next(set(input_) for input_ in inputs if len(input_) == 2)
    digits[4] = next(set(input_) for input_ in inputs if len(input_) == 4)
    digits[7] = next(set(input_) for input_ in inputs if len(input_) == 3)
    digits[8] = next(set(input_) for input_ in inputs if len(input_) == 7)

    five_lens = (set(input_) for input_ in inputs if len(input_) == 5)
    for five_len in five_lens:
        if digits[1].issubset(five_len):
            digits[3] = five_len
        elif len(digits[4] & five_len) == 3:
            digits[5] = five_len
        else:
            digits[2] = five_len
    six_lens = (set(input_) for input_ in inputs if len(input_) == 6)
    for six_len in six_lens:
        if len(six_len & digits[4]) == 4:
            digits[9] = six_len
        elif len(six_len & digits[5]) == 5:
            digits[6] = six_len
        else:
            digits[0] = six_len

    value = 0
    for output in outputs:
        value = value * 10 + digits.index(set(output))
    output_sums += value

print(output_sums)
