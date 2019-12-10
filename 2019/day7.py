import itertools

from utils import get_input_lines


numbers = list(map(int, next(get_input_lines(__file__)).split(',')))
op_fns = {
    1: lambda a, b: a + b,
    2: lambda a, b: a * b,
    5: lambda a, b, i: b if a != 0 else i + 3,
    6: lambda a, b, i: b if a == 0 else i + 3,
    7: lambda a, b: 1 if a < b else 0,
    8: lambda a, b: 1 if a == b else 0,
}


def process(nums, input_iter):
    i = 0
    while i < len(nums) and nums[i] != 99:
        opcode = nums[i] % 100
        param_modes = [nums[i] // k % 10 for k in [100, 1000, 10000]]

        def arg(n):
            return nums[nums[i + n + 1]] if param_modes[n] == 0 else nums[i + n + 1]
        a = arg(0)

        if opcode in (1, 2, 7, 8):
            b = arg(1)
            c = nums[i + 3]
            nums[c] = op_fns[opcode](a, b)
            i += 4
        elif opcode in (3, 4):
            if opcode == 3:
                nums[nums[i + 1]] = next(input_iter)
            else:
                yield a
            i += 2
        elif opcode in (5, 6):
            b = arg(1)
            i = op_fns[opcode](a, b, i)


max_out = -1
for phase in itertools.permutations([9, 8, 7, 6, 5]):
    outputs = {}
    inputs = {}

    for i in range(5):
        inputs[i] = [phase[i]]
        if i == 0:
            inputs[i].append(0)
        outputs[i] = process(numbers.copy(), iter(inputs[i]))

    try:
        while True:
            for i in range(5):
                out = next(outputs[i])
                if i == 4:
                    max_out = max(out, max_out)
                inputs[(i + 1) % 5].append(out)
    except StopIteration:
        pass

print(max_out)
