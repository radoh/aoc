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


def process(nums, input):
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
            nums[a] = next(input)
            i += 2
        elif opcode == 4:
            a = arg(0, False)
            yield a
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


inputs = []
num_dict = collections.defaultdict(int, {i: n for i, n in enumerate(numbers)})
out = process(num_dict, iter(inputs))
pos = (0, 0)
m = collections.defaultdict(int)
m[pos] = 1
d = '^'
dr = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
dl = {'^': '<', '>': '^', 'v': '>', '<': 'v'}
do = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
try:
    while True:
        inputs.append(m[pos])
        paint = next(out)
        turn = next(out)
        m[pos] = paint
        d = dr[d] if turn else dl[d]
        pos = pos[0] + do[d][0], pos[1] + do[d][1]
except StopIteration:
    pass

print(len(m.keys()))

for r in range(max(map(lambda e: e[0], m.keys())) + 1):
    for c in range(max(map(lambda e: e[1], m.keys())) + 1):
        print('█' if m[(r, c)] else ' ', end='')
    print()



