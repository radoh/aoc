from utils import get_input_lines


def update(ctx, **kwargs):
    ctx.update(kwargs)
    return ctx

pointer = 0
fns = {
    'nop': lambda ctx, x: update(ctx, pointer=ctx['pointer'] + 1),
    'jmp': lambda ctx, x: update(ctx, pointer=ctx['pointer'] + x),
    'acc': lambda ctx, x: update(ctx, acc=ctx['acc'] + x, pointer=ctx['pointer'] + 1),
}

program = []
for l in get_input_lines(__file__):
    instr, num_str = l.split(' ')
    program.append((fns[instr], int(num_str)))

ctx = dict(pointer=0, acc=0)
pointers = set()
while True:
    pointer = ctx['pointer']
    if pointer in pointers:
        print(ctx['acc'])
        break
    pointers.add(pointer)
    fn, arg = program[pointer]
    ctx = fn(ctx, arg)


def program_permutation(instructions):
    for i, instr in enumerate(instructions):
        fn, arg = instr
        if fn in [fns['nop'], fns['jmp']]:
            new_program = instructions.copy()
            new_program[i] = (fns['jmp'], arg) if fn == 'nop' else (fns['nop'], arg)
            yield new_program


for prg in program_permutation(program):
    ctx = dict(pointer=0, acc=0)
    pointers = set()
    fail = False
    while ctx['pointer'] < len(prg):
        pointer = ctx['pointer']
        if pointer in pointers:
            fail = True
            break
        pointers.add(pointer)
        fn, arg = prg[pointer]
        ctx = fn(ctx, arg)
    if not fail:
        print(ctx['acc'])
