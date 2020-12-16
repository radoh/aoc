import math
import re

from utils import get_input_lines

lines = get_input_lines(__file__)

type_ranges = {}
for l in lines:
    m = re.match(r'^([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)$', l)
    if not m:
        break
    type, a, b, c, d = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))
    type_ranges[type] = ((a, b), (c, d))

next(lines)
my_ticket = list(map(int, next(lines).split(',')))

next(lines)
next(lines)
nearby = [list(map(int, l.split(','))) for l in lines]

def check_range(n, r):
    (a, b), (c, d) = r
    return a <= n <= b or c <= n <= d

invalid_sum = 0
valid_tickets = []
for near in nearby:
    is_valid = True
    for n in near:
        if all(not check_range(n, r) for r in type_ranges.values()):
            is_valid = False
            invalid_sum += n
    if is_valid:
        valid_tickets.append(near)

print(invalid_sum)

matched = {}
available = set(type_ranges.keys())
while len(available) > 0:
    for i in range(len(type_ranges.keys())):
        range_candidates = available.copy()
        for n_row in valid_tickets:
            for range_type in list(range_candidates):
                r = type_ranges[range_type]
                if not check_range(n_row[i], r):
                    range_candidates.remove(range_type)
        if len(range_candidates) == 1:
            matched[next(iter(range_candidates))] = i
            available.remove(next(iter(range_candidates)))

print(math.prod(my_ticket[v] for k, v in matched.items() if k.startswith('departure')))