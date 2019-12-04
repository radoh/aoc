from utils import get_input_lines


def f(n):
    n = n // 3 - 2
    return n + f(n) if n > 0 else 0


total = 0
total2 = 0
for l in get_input_lines(__file__):
    mass = int(l)
    total += mass // 3 - 2
    total2 += f(mass)

print(total)
print(total2)
