import operator
from collections import defaultdict
from functools import reduce

from utils import get_input_lines

trees = defaultdict(int)
for i, row in enumerate(get_input_lines(__file__)):
    for offset in [1, 3, 5, 7]:
        if row[offset * i % len(row)] == '#':
            trees[offset] += 1
    if i % 2 == 0 and row[i // 2 % len(row)] == '#':
        trees[2] += 1

print(trees[3])
print(reduce(operator.mul, trees.values()))