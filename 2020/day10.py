from collections import Counter

from utils import get_input_lines

nums = sorted([int(l) for l in get_input_lines(__file__)])
nums = [0] + nums + [max(nums) + 3]

diffs = Counter()
for a, b in zip(nums[:-1], nums[1:]):
    diffs.update({(b - a): 1})
print(diffs[1] * diffs[3])

choices = {}
for n in reversed(nums):
    choices[n] = sum(choices[k] for k in filter(lambda x: 1 <= x - n <= 3, nums)) or 1
print(choices[0])
