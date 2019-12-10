from collections import defaultdict

from utils import get_input_lines


orbits = get_input_lines(__file__)


class P:
    def __init__(self, name) -> None:
        self.name = name
        self.children = []
        self.orbits = None


orbs = {}
for r in orbits:
    a, b = r.split(')')
    a, b = orbs.get(a, P(a)), orbs.get(b, P(b))
    a.children.append(b)
    b.orbits = a
    if a not in orbs:
        orbs[a.name] = a
    if b not in orbs:
        orbs[b.name] = b

total = 0
for name, orb in orbs.items():
    o = orb
    while orb.orbits is not None:
        orb = orb.orbits
        total +=1
print(total)

vals = defaultdict(int)
o = orbs['SAN'].orbits
vals[o.name] = 0
t = 1
while o.orbits is not None:
    o = o.orbits
    vals[o.name] = t
    t +=1

o = orbs['YOU'].orbits
t = 0
while o.name not in vals:
    o = o.orbits
    t +=1

print(vals[o.name] + t)

