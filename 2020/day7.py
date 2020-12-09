import re
import networkx as nx
from utils import get_input_lines

g = nx.DiGraph()
for l in get_input_lines(__file__):
    main, contents = l.split('contain')
    color1 = re.match(r'^([a-z ]+) bag', l).group(1)
    for count, color in re.findall(r'(\d+) ([a-z ]+) bag', contents):
        g.add_edge(color1, color, weight=int(count))

def predecessors(g, target, s):
    for pred in g.predecessors(target):
        s.add(pred)
        predecessors(g, pred, s)
    return s

print(len(predecessors(g, 'shiny gold', set())))

def total_bag(g, source):
    if not list(g.successors(source)):
        return 1
    return 1 + sum(g.get_edge_data(source, succ)['weight'] * total_bag(g, succ) for succ in g.successors(source))

print(total_bag(g, 'shiny gold') - 1)
