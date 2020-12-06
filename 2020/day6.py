from collections import Counter

from utils import get_input_lines

groups = [Counter()]
for l in get_input_lines(__file__):
    if l:
        groups[-1].update(l, size=1)
    else:
        groups.append(Counter())

print(sum(len(c.keys()) - 1 for c in groups))

print(sum(sum(int(v == c['size']) for k, v in c.items()) - 1 for c in groups))
