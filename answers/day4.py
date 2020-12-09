import re


with open('../input_files/day4') as f:
    data = f.read().split('\n\n')
    data = [dict(entry.split(':') for entry in item.split()) for item in data]

keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
print(sum(not keys - pport.keys() for pport in data))

valid_pports = 0
for pport in data:
    valid_pports += \
        not keys - pport.keys() and \
        all((1920 <= int(pport['byr']) <= 2002,
             2010 <= int(pport['iyr']) <= 2020,
             2020 <= int(pport['eyr']) <= 2030,
             (pport['hgt'].endswith('cm') and 150 <= int(pport['hgt'][:-2]) <= 193) or
             (pport['hgt'].endswith('in') and 59 <= int(pport['hgt'][:-2]) <= 76),
             re.match(r'^#[\da-f]{6}$', pport['hcl']),
             pport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
             re.match(r'^\d{9}$', pport['pid'])))
print(valid_pports)
