from utils import get_input_lines

input = get_input_lines(__file__)
depart_at = int(next(input))

lines = {
    int(line): offset
    for offset, line in enumerate(next(input).split(',')) if line != 'x'
}


i = depart_at
while True:
    available = list(filter(lambda n: i % n == 0, lines.keys()))
    if available:
        print(available[0] * (i - depart_at))
        break
    i += 1


def verify(timestamp, lines):
    return all((timestamp + off) % l == 0 for l, off in lines.items())


def incremental_subdicts(d):
    new_dict = {}
    for k, v in d.items():
        new_dict[k] = v
        yield {**new_dict}

i = 1
increment = 1
for d in incremental_subdicts(lines):
    success_at = []
    while True:
        if verify(i, d):
            success_at.append(i)
            if len(success_at) > 1:
                increment = success_at[1] - success_at[0]
                break
        i += increment
    print(f'for lines {d} = {success_at[0]}')
