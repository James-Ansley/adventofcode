import re

instruction_regex = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")

with open("input_files/day03", "r") as f:
    instructions = instruction_regex.findall(f.read())

total = 0
switched_total = 0

do_multiply = True
for instruction in instructions:
    if instruction == "do()":
        do_multiply = True
    elif instruction == "don't()":
        do_multiply = False
    else:
        left, right = instruction[4:-1].split(",")
        product = int(left) * int(right)
        total += product
        if do_multiply:
            switched_total += product

print(total)
print(switched_total)
