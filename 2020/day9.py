import itertools
from utils import get_input_lines

nums = [int(l) for l in get_input_lines(__file__)]


def try_sum(numbers, num):
    return any(a != b and a + b == num for a, b in itertools.product(numbers, numbers))


for i, n in enumerate(nums[25:]):
    if not try_sum(nums[i: i + 25], n):
        print(f'{n} not possible')
        target = n
        nums.remove(target)
        break

for i in range(len(nums)):
    for j, total in enumerate(itertools.accumulate(nums[i:])):
        if total == target:
            print(min(nums[i:j + i + 1]) + max(nums[i:j + i + 1]))
            break
