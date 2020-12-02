import re
from collections import Counter

from utils import get_input_lines

valid = 0
valid2 = 0
for l in get_input_lines(__file__):
    m = re.match(r'^(\d+)-(\d+) ([a-z]): ([a-z]+).*$', l)
    a, b, char, word = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
    if a <= Counter(word)[char] <= b:
        valid += 1
    if (word[a - 1] == char) != (word[b - 1] == char):
        valid2 += 1

print(valid)
print(valid2)