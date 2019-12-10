import collections
import itertools

from utils import get_input_lines


numbers = next(get_input_lines(__file__))
cols = 25
rows = 6

layers = []
min_layer_sum = 0
min_layer_count = 999999
for l in range(len(numbers) // (cols * rows)):
    counter = collections.Counter(numbers[l * cols * rows: l * cols * rows + cols * rows])
    if counter['0'] < min_layer_count:
        min_layer_sum = counter['1'] * counter['2']
        min_layer_count = counter['0']

    rs = [
        numbers[l * cols * rows + r * cols:l * cols * rows + r * cols + cols]
        for r in range(rows)
    ]
    layers.append(rs)

print(min_layer_sum)

for r in range(rows):
    for c in range(cols):
        pixel = next(itertools.dropwhile(lambda x: x == '2', map(lambda l: l[r][c], layers)))
        print('█' if pixel == '1' else ' ', end='')
    print()
