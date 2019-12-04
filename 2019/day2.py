from utils import get_input_lines
import itertools


numbers = list(map(int, next(get_input_lines(__file__)).split(',')))
numbers[1] = 12
numbers[2] = 2


def process(nums):
    i = 0
    while nums[i] != 99:
        a, b = nums[nums[i + 1]], nums[nums[i + 2]]
        nums[nums[i + 3]] = a + b if nums[i] == 1 else a * b
        i += 4
    return nums


result = process(numbers.copy())
print(result[0])

for a, b in itertools.product(range(0, 100), range(0, 100)):
    numbers[1] = a
    numbers[2] = b
    try:
        result = process(numbers.copy())
    except IndexError:
        continue
    if result[0] == 19690720:
        print(100 * a + b)
        break
