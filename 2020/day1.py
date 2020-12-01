import itertools

from utils import get_input_lines

nums = [int(l) for l in get_input_lines(__file__)]

for a, b in itertools.product(nums, nums):
    if a + b == 2020:
        print(a * b)
        break

for a, b, c in itertools.product(nums, nums, nums):
    if a + b + c == 2020:
        print(a * b * c)
        break
