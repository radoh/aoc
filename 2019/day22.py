import math

from itertools import count
from utils import get_input_lines, modinv


lines = list(get_input_lines(__file__))


def rev(l):
    return list(reversed(l))


def cut(l, n):
    return l[n:] + l[0: n]


def inc_deal(l, inc):
    k = l.copy()
    n = len(k)
    for i, pos in zip(range(n), count(start=0, step=inc)):
        k[pos % n] = l[i]
    return k



MAX = 119315717514047


def optimize_2fns(fn1_arg, fn2_arg):
    fn1, fn2, fn1a, fn2a = fn1_arg[0], fn2_arg[0], fn1_arg[1] if len(fn1_arg) > 1 else None, fn2_arg[1] if len(fn2_arg) > 1 else None

    if fn1 == rev and fn2 == rev:
        return []
    if fn1 == cut and fn2 == cut:
        return [(cut, (fn1a + fn2a) % MAX)]
    if fn1 == inc_deal and fn2 == inc_deal:
        return [(inc_deal, (fn1a * fn2a) % MAX)]

    if fn1 == rev and fn2 == cut:
        return [(cut, (MAX - fn2a) % MAX), (rev, )]
    if fn1 == cut and fn2 == inc_deal:
        return [(inc_deal, fn2a), (cut, fn1a * fn2a % MAX)]
    if fn1 == rev and fn2 == inc_deal:
        return [(inc_deal, fn2a), (cut, -fn2a + 1), (rev, )]

    return None


fns = []
for l in lines:
    if l == 'deal into new stack':
        fns.append((rev, ))
    elif l.startswith('deal with increment '):
        fns.append((inc_deal, int(l[20:])))
    elif l.startswith('cut '):
        fns.append((cut, int(l[4:])))
    else:
        raise RuntimeError


def optimize(fn_list):
    optimized = fn_list.copy()
    while True:
        skip_next = False
        opt = []
        res = None
        for i, (fn1, fn2) in enumerate(zip(optimized, optimized[1:])):
            if skip_next:
                skip_next = False
                res = None
                continue
            res = optimize_2fns(fn1, fn2)
            if res is None:
                opt.append(fn1)
            else:
                opt += res
                skip_next = True
        if res is None:
            opt.append(optimized[-1])
        if opt == optimized:
            break
        optimized = opt
    return optimized

optimized = optimize(fns)

ITERS = 101741582076661
iter_fns = {1: optimized}
opt = optimized.copy()
for i in range(1, int(math.log2(ITERS)) + 1):
    opt = optimize(opt * 2)
    iter_fns[2 ** i] = opt


def part1():
    nums = list(range(0, 10007))
    for fn, *args in fns:
        nums = fn(nums, *args)
    print('part1:', nums.index(2019))
part1()

iters = ITERS
applied_fns = []
while iters > 0:
    log2 = int(math.log2(iters))
    for fn, *args in iter_fns[2 ** log2]:
        applied_fns.append((fn, *args))

    iters -= 2 ** log2

num_on_pos_2020 = 2020
for fn, *args in reversed(applied_fns):
    if fn == rev:
        num_on_pos_2020 = MAX - num_on_pos_2020 - 1
    elif fn == inc_deal:
        k = args[0]
        num_on_pos_2020 = ((num_on_pos_2020 // k) % MAX if num_on_pos_2020 % k == 0 else (modinv(k, MAX) * num_on_pos_2020 % MAX)) if k > 0 else num_on_pos_2020
    elif fn == cut:
        k = args[0]
        num_on_pos_2020 = (num_on_pos_2020 + k) % MAX
print('part2:', num_on_pos_2020)

