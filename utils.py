import os


def input_fn(filename):
    return f'{os.path.basename(filename).split(".")[0]}.in'


def get_input_lines(filename):
    return get_lines(input_fn(filename))


def get_lines(filename):
    for line in open(filename):
        yield line.rstrip('\n')


def get_num(filename, delim=' '):
    for line in open(filename):
        for num_str in line.split(delim):
            yield int(num_str)


def clear():
    import os
    os.system('clear')

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
