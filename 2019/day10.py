from utils import get_input_lines
import math


lines = get_input_lines(__file__)
asteroids = set()
cols = 0
for r, l in enumerate(lines):
    for c, el in enumerate(l):
        if el != '.':
            asteroids.add((r, c))
        cols = c + 1
    rows = r + 1


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def any_in_line(start, target):
    row, col = start
    r, c = target
    dr, dc = r - row, c - col
    a = gcd(abs(dr), abs(dc))
    vr, vc = dr // a, dc // a
    for i in range(1, a):
        nr, nc = row + vr * i, col + vc * i
        if (nr, nc) != (r, c) and (nr, nc) in asteroids:
            return True
    return False


def from_start(row, col):
    total = 0
    for r, c in asteroids:
        if (r, c) == (row, col):
            continue
        total += 0 if any_in_line((row, col), (r, c)) else 1
    return total


def angle(a, b, c, clockwise=True):
    ab, cb = math.atan2(a[1]-b[1], a[0]-b[0]), math.atan2(c[1]-b[1], c[0]-b[0])
    ang = math.degrees((ab - cb) if clockwise else (cb - ab))
    return ang + 360 if ang < 0 else ang


def find_next(last_angle, max_rc):
    north = (-1, max_rc[1])
    min_angle = 999
    asteroid = None
    for r, c in asteroids:
        a = angle(north, max_rc, (r, c))
        if a < min_angle and (a > last_angle) and not any_in_line(max_rc, (r, c)):
            min_angle = a
            asteroid = (r, c)
    return min_angle, asteroid


def calc():
    max_out, max_rc = 0, None
    for r, c in asteroids:
        n = from_start(r, c)
        max_out, max_rc = max((max_out, max_rc), (n, (r, c)))

    print(f'max: {max_rc} = {max_out}')

    asteroids.remove(max_rc)
    i = 0
    last_angle = -1
    while i < 200:
        min_angle, asteroid = find_next(last_angle, max_rc)
        if asteroid is None:
            min_angle, asteroid = find_next(-1, max_rc)
        assert asteroid
        # print(f'removing asteroid #{i} at {asteroid} in angle {min_angle} (last angle: {last_angle})')
        asteroids.remove(asteroid)
        last_angle = min_angle
        i += 1
    print(asteroid[1] * 100 + asteroid[0])


calc()
