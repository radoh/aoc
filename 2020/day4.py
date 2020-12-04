import re
from utils import get_input_lines

passports = [{}]
for l in get_input_lines(__file__):
    if l:
        passports[-1].update(dict([tuple(kv.split(':')) for kv in l.split(' ')]))
    else:
        passports.append({})

print(passports)
required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',}

valid = sum(int(all(r in p for r in required)) for p in passports)
print(valid)

validation_fns = {
    'byr': lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
    'iyr': lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
    'eyr': lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
    'hgt': lambda x: re.match(r'^\d+(cm|in)$', x) and 150 <= int(x.replace('cm', '')) <= 193 if 'cm' in x else 59 <= int(x.replace('in', '')) <= 76,
    'hcl': lambda x: re.match(r'^#[a-f0-9]{6}$', x),
    'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda x: re.match(r'^\d{9}$', x),
    # cid = lambda x: True
}

valid2 = sum(int(all(fieldname in p and fn(p[fieldname]) for fieldname, fn in validation_fns.items())) for p in passports)
print(valid2)
