input_range = range(206938, 679128 + 1)


def two_digits_same(n, part1=False):
    for i in range(1, 10):
        if f'{i}{i}' in n and (part1 or f'{i}{i}{i}' not in n):
            return True
    return False


def dont_decrease(n):
    return sorted(n) == list(n)


print(sum(1 for i in map(str, input_range) if two_digits_same(i, True) and dont_decrease(i)))
print(sum(1 for i in map(str, input_range) if two_digits_same(i, False) and dont_decrease(i)))