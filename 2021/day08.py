import re

with open('input_files/day08') as f:
    data = re.findall(r'(.*) \| (.*)', f.read())
    data = [(ins.split(), outs.split()) for ins, outs in data]

uniques = 0
for _, outs in data:
    uniques += sum(len(output) in (2, 3, 4, 7) for output in outs)

print(uniques)

output_sums = 0
for ins, outs in data:
    digits = [set()] * 10
    digits[1] = next(set(in_) for in_ in ins if len(in_) == 2)
    digits[4] = next(set(in_) for in_ in ins if len(in_) == 4)
    digits[7] = next(set(in_) for in_ in ins if len(in_) == 3)
    digits[8] = next(set(in_) for in_ in ins if len(in_) == 7)

    five_lens = (set(in_) for in_ in ins if len(in_) == 5)
    for five_len in five_lens:
        if digits[1].issubset(five_len):
            digits[3] = five_len
        elif len(digits[4] & five_len) == 3:
            digits[5] = five_len
        else:
            digits[2] = five_len
    six_lens = (set(in_) for in_ in ins if len(in_) == 6)
    for six_len in six_lens:
        if len(six_len & digits[4]) == 4:
            digits[9] = six_len
        elif len(six_len & digits[5]) == 5:
            digits[6] = six_len
        else:
            digits[0] = six_len

    value = 0
    for out in outs:
        value = value * 10 + digits.index(set(out))
    output_sums += value

print(output_sums)
