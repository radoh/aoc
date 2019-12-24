import copy

from utils import get_input_lines


lines = get_input_lines(__file__)
m = []
for l in lines:
    m.append(list(l))
R, C = len(m), len(m[0])
orig = copy.deepcopy(m)


def simulate(m):
    newm = []
    for r, row in enumerate(m):
        newm.append([])
        for c, cell in enumerate(row):
            bug_count = 0
            for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= R or nc >= C:
                    continue
                bug_count += 1 if m[nr][nc] == '#' else 0
            if cell == '#' and bug_count != 1:
                cell = '.'  # dies
            elif cell == '.' and bug_count in (1, 2):
                cell = '#'  # spawns new
            newm[r].append(cell)
    return newm


def draw(m):
    for r in m:
        print(''.join(r))
    print()


def custom_hash(m):
    pow2 = 1
    rating = 0
    for r in m:
        for c in r:
            if c == '#':
                rating += pow2
            pow2 *= 2
    return rating



seen = {custom_hash(m)}
tick = 0
print(f'#{tick}')
draw(m)
while True:
    tick += 1
    m = simulate(m)
    h = custom_hash(m)
    print(f'#{tick}')
    draw(m)
    if h in seen:
        print(f'#{tick} already appeared, hash: {h}')
        break
    seen.add(h)

empty = [['.' for _ in range(C)] for _ in range(R)]
all = {level: copy.deepcopy(empty) for level in range(-210, 210)}
all[0] = copy.deepcopy(orig)


border_cells = {
    (-1, 0): [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), ],
    (0, 1): [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), ],
    (1, 0): [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), ],
    (0, -1): [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), ],
}
def simulate_level(level, m, other):
    newm = []
    for r, row in enumerate(m):
        newm.append([])
        for c, cell in enumerate(row):
            bug_count = 0
            for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)) if (r, c) != (2, 2) else ():
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= R or nc >= C:
                    other_cell = other[level + 1][2 + dr][2 + dc] if level + 1 in other else '.'
                elif (nr, nc) == (2, 2):
                    for nr, nc in (border_cells[(dr, dc)] if level - 1 in other else []):
                        if other[level - 1][nr][nc] == '#':
                            bug_count += 1
                    continue
                else:
                    other_cell = m[nr][nc]
                bug_count += 1 if other_cell == '#' else 0
            if cell == '#' and bug_count != 1:
                cell = '.'  # dies
            elif cell == '.' and bug_count in (1, 2):
                cell = '#'  # spawns new
            newm[r].append(cell)
    return newm


def simulate_all(all):
    new_all = {}
    for level, m in all.items():
        new_all[level] = simulate_level(level, m, all)
    return new_all


for tick in range(0, 200):
    all = simulate_all(all)

# for level in range(-5, 5):
#     print(f'level: {level}')
#     draw(all[level])


total_bug_count = 0
for level in range(-200, 200):
    for row in all[level]:
        for cell in row:
            if cell == '#':
                total_bug_count += 1
print(f'total bug count: {total_bug_count}')
