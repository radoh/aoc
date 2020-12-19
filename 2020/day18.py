import functools
import operator

from utils import get_input_lines


def calc(i, tok):
    vals = []
    ops = []
    while i < len(tok):
        t = tok[i]
        if t.isnumeric():
            vals.append(int(t))
        elif t == '(':
            i, res = calc(i + 1, tok)
            vals.append(res)
        elif t == ')':
            break
        else:
            ops.append(operator.add if t == '+' else operator.mul)
        i += 1
    val = functools.reduce(lambda a, e: e[1](a, e[0]), zip(vals[1:], ops), vals[0])
    return i, val


total = 0
for l in get_input_lines(__file__):
    tokens = l.replace('(', '( ').replace(')', ' )').split(' ')
    res = calc(0, tokens)
    total += res[1]
print(total)



def calc2(i, tok):
    vals = []
    ops = []
    while i < len(tok):
        t = tok[i]
        if t.isnumeric():
            vals.append(int(t))
        elif t == '(':
            i, res = calc2(i + 1, tok)
            vals.append(res)
        elif t == ')':
            break
        else:
            ops.append(operator.add if t == '+' else operator.mul)
        i += 1
    new_vals = []
    val = vals[0]
    for num, op in zip(vals[1:], ops):
        if op == operator.mul:
            new_vals.append(val)
            val = num
        else:
            val += num
    val = functools.reduce(lambda a, e: e[1](a, e[0]), zip(new_vals[1:], filter(lambda x: x == operator.mul, ops)), new_vals[0])
    return i, val


total = 0
for l in get_input_lines(__file__):
    tokens = l.replace('(', '( ').replace(')', ' )').split(' ')
    res = calc2(0, tokens)
    total += res[1]
print(total)
