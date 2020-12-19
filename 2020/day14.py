import itertools
import re

from utils import get_input_lines

def mask_number(mask, n, version=1):
    return int(''.join(
        (b if a == 'X' else a) if version == 1 else ('0' if a == '2' else ('1' if a == '1' else b))
        for a, b in zip(mask, f'{bin(n)[2:]:0>36}')
    ), 2)


mask = ''
mem = {}
for l in get_input_lines(__file__):
    m = re.match(r'^mask = ([0-9X]+)$', l)
    if m:
        mask = m.group(1)
    else:
        m = re.match(r'^mem\[(\d+)] = (\d+)$', l)
        addr, val = int(m.group(1)), int(m.group(2))
        mem[addr] = mask_number(mask, val)

print(sum(mem.values()))


def mask_address(mask, address):
    choices = [['2', '1'] for _ in range(mask.count('X'))]
    for bits in itertools.product(*choices):
        mask2 = mask
        for bit in bits:
            mask2 = mask2.replace('X', bit, 1)
        yield mask_number(mask2, address, version=2)


mask = ''
mem = {}
for l in get_input_lines(__file__):
    m = re.match(r'^mask = ([0-9X]+)$', l)
    if m:
        mask = m.group(1)
    else:
        m = re.match(r'^mem\[(\d+)] = (\d+)$', l)
        addr, val = int(m.group(1)), int(m.group(2))
        for address in mask_address(mask, addr):
            mem[address] = val

print(sum(mem.values()))