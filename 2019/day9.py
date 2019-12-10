from utils import get_input_lines
import collections


numbers = list(map(int, next(get_input_lines(__file__)).split(',')))
op_fns = {
    1: lambda a, b: a + b,
    2: lambda a, b: a * b,
    5: lambda a, b, i: b if a != 0 else i + 3,
    6: lambda a, b, i: b if a == 0 else i + 3,
    7: lambda a, b: 1 if a < b else 0,
    8: lambda a, b: 1 if a == b else 0,
}


def process(nums, system_id):
    i = 0
    relative = [0]
    while nums[i] != 99:
        opcode = nums[i] % 100
        param_modes = [nums[i] // k % 10 for k in [100, 1000, 10000]]

        def arg(n, is_out):
            if param_modes[n] == 2:
                return nums[relative[0] + nums[i + n + 1]] if not is_out else relative[0] + nums[i + n + 1]
            return nums[nums[i + n + 1]] if param_modes[n] == 0 and not is_out else nums[i + n + 1]

        if opcode in (1, 2, 7, 8):
            a = arg(0, False)
            b = arg(1, False)
            c = arg(2, True)
            nums[c] = op_fns[opcode](a, b)
            i += 4
        elif opcode == 3:
            a = arg(0, True)
            nums[a] = system_id
            i += 2
        elif opcode == 4:
            a = arg(0, False)
            print(a)
            i += 2
        elif opcode in (5, 6):
            a = arg(0, False)
            b = arg(1, False)
            i = op_fns[opcode](a, b, i)
        elif opcode == 9:
            a = arg(0, False)
            relative[0] += a
            i += 2

    return nums


num_dict = collections.defaultdict(int, {i: n for i, n in enumerate(numbers)})
result = process(num_dict, 1)

num_dict = collections.defaultdict(int, {i: n for i, n in enumerate(numbers)})
result = process(num_dict, 2)
