import itertools

from utils import get_input_lines


cubes = set()
cubes4 = set()
for y, l in enumerate(get_input_lines(__file__)):
    for x, k in enumerate(l):
        if k == '#':
            cubes.add((x, y, 0))
            cubes4.add((x, y, 0, 0))
N = y + 1

def neighbours(x, y, z):
    for ox, oy, oz in itertools.product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]):
        nx, ny, nz = x + ox, y + oy, z + oz
        if (nx, ny, nz) != (x, y, z):
            yield nx, ny, nz

def neighbours4(x, y, z, w):
    for ox, oy, oz, ow in itertools.product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1]):
        nx, ny, nz, nw = x + ox, y + oy, z + oz, w + ow
        if (nx, ny, nz, nw) != (x, y, z, w):
            yield nx, ny, nz, nw


cycle = 0
while cycle < 6:
    new_cubes = set()
    for x, y, z in itertools.product(range(-(cycle + 1), N + 1 + cycle), range(-(cycle + 1), N + 1 + cycle), range(-(cycle + 1), 0 + 1 + cycle + 1)):
        active_count = 0
        for nx, ny, nz in neighbours(x, y, z):
            if (nx, ny, nz) in cubes:
                active_count += 1
        if (x, y, z) in cubes and 2 <= active_count <= 3:
            new_cubes.add((x, y, z))
        elif (x, y, z) not in cubes and active_count == 3:
            new_cubes.add((x, y, z))
    cubes = new_cubes
    cycle += 1
print('count', len(cubes))

cycle = 0
cubes = cubes4.copy()
while cycle < 6:
    new_cubes = set()
    for x, y, z, w in itertools.product(range(-(cycle + 1), N + 1 + cycle), range(-(cycle + 1), N + 1 + cycle), range(-(cycle + 1), 0 + 1 + cycle + 1), range(-(cycle + 1), 0 + 1 + cycle + 1)):
        active_count = 0
        for nx, ny, nz, nw in neighbours4(x, y, z, w):
            if (nx, ny, nz, nw) in cubes:
                active_count += 1
        if (x, y, z, w) in cubes and 2 <= active_count <= 3:
            new_cubes.add((x, y, z, w))
        elif (x, y, z, w) not in cubes and active_count == 3:
            new_cubes.add((x, y, z, w))
    cubes = new_cubes
    cycle += 1
print('count', len(cubes))