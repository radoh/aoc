import re

from utils import get_input_lines


OFFSETS = {
    'sw': (1, -1),
    'se': (1, 0),
    'nw': (-1, 0),
    'ne': (-1, 1),
    'e': (0, 1),
    'w': (0, -1),
}


def get_coord(instr):
    r, c = 0, 0
    for d in filter(None, re.split(r'(sw|se|ne|nw|w|e)', instr)):
        r, c = r + OFFSETS[d][0], c + OFFSETS[d][1]
    return r, c


flipped = set()
for l in get_input_lines(__file__):
    coord = get_coord(l)
    if coord in flipped:
        flipped.remove(coord)
    else:
        flipped.add(coord)

print(len(flipped))

maxr, maxc, minr, minc = max(r for r, c in flipped), max(c for r, c in flipped), min(r for r, c in flipped), min(c for r, c in flipped)
for day in range(100):
    new_flipped = flipped.copy()
    for r in range(minr - 1, maxr + 2):
        for c in range(minc - 1, maxc + 2):
            black = sum(1 if (r + offr, c + offc) in flipped else 0 for offr, offc in OFFSETS.values())
            if (r, c) in flipped and (black == 0 or black > 2):
                new_flipped.remove((r, c))
            elif (r, c) not in flipped and black == 2:
                new_flipped.add((r, c))
                maxr, maxc, minr, minc = max(maxr, r), max(maxc, c), min(minr, r), min(minc, c)
    flipped = new_flipped

print(len(flipped))