import re
from collections import Counter
from utils import get_input_lines

rules = {}
messages = []
for l in get_input_lines(__file__):
    if m := re.match(r'^(\d+): (.+)$', l):
        rules[int(m.group(1))] = m.group(2).replace('"', '')
    elif l:
        messages.append(l)


def inline_rules(s, replace_limits=0):
    s = f' {s} '
    replace_counts = Counter()
    while m := re.search(r'(\d+)', s):
        num = int(m.group(1))
        if replace_limits and num in [8, 11]:
            if replace_counts[num] <= replace_limits:
                s = re.sub(f' {num} ', f' ( {rules[num]} ) ', s)
                replace_counts.update({num: 1})
            else:
                s = re.sub(f' {num} ', ' X ' if num == 8 else ' Y ', s)
        else:
            s = re.sub(f' {num} ', f' ( {rules[num]} ) ', s)
    s = s.replace('"', '').replace(' ', '').replace('(a)', 'a').replace('(b)', 'b')
    return s


rule_them_all = inline_rules(rules[0])
print(sum(1 if re.fullmatch(rule_them_all, message) else 0 for message in messages))

rules[8] = '42 | 42 8'
rules[11] = '42 31 | 42 11 31'

rule_them_all = inline_rules(rules[0], replace_limits=4)
print(sum(1 if re.fullmatch(rule_them_all, message) else 0 for message in messages))
