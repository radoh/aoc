from utils import get_input_lines


def find_row(instructions, lower, upper):
    instr = next(instructions, None)
    if instr is None:
        return lower
    if instr in ('F', 'L'):
        return find_row(instructions, lower, upper - (upper - lower + 1) // 2)
    return find_row(instructions, lower + (upper - lower + 1) // 2, upper)


def seat_id(l):
    row = find_row(iter(l[:7]), 0, 127)
    col = find_row(iter(l[7:]), 0, 8)
    return row * 8 + col


seat_ids = [int(seat_id(l)) for l in get_input_lines(__file__)]
max_id = max(seat_ids)
print(f'max id: {max_id}')

ids = list(sorted(seat_ids))
last_i = ids[0] - 1
for i in ids:
    if last_i + 1 != i:
        print(f'my id: {last_i + 1}')
    last_i = i
