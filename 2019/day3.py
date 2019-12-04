from utils import get_input_lines


lines = get_input_lines(__file__)
line1, line2 = next(lines).split(','), next(lines).split(',')
Dx = dict(U=0, R=1, D=0, L=-1)
Dy = dict(U=-1, R=0, D=1, L=0)


def draw(line):
    dstxy = {}
    x, y = 0, 0
    step_counter = 0
    for cmd in line:
        d, steps = cmd[0], int(cmd[1:])
        for _ in range(steps):
            step_counter += 1
            x, y = x + Dx[d], y + Dy[d]
            if (x, y) not in dstxy:
                dstxy[(x, y)] = step_counter
    return dstxy


dstxy1, dstxy2 = draw(line1), draw(line2)
crossed = set(dstxy1.keys()).intersection(set(dstxy2.keys()))
min_dist = 9999999
min_steps = 9999999
for x, y in crossed:
    dst = abs(x) + abs(y)
    min_dist = min(min_dist, dst)
    steps_sum = dstxy1[(x, y)] + dstxy2[(x, y)]
    min_steps = min(min_steps, steps_sum)
print(min_dist)
print(min_steps)
