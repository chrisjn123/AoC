from collections import defaultdict

with open('input.txt', 'r') as fh:
    data = fh.readlines()


class Valve:
    def __init__(self, name:str, flow: int, conns:list) -> None:
        self.name = name
        self.flow = flow
        self.connections = conns
        self.open = False

g = defaultdict(list)
open_valves = defaultdict()
flow = defaultdict()

name_table = defaultdict(int)
name_v = 0

for line in data:
    sp = line.split(';')
    name = sp[0].split()[1]
    name_table[name] = name_v
    name_v += 1
    value = int(sp[0].split('=')[-1])

    conns = sp[1].split('valve')[1]
    conns = conns.replace('s','').strip()
    connections = conns.split(',')
    
    v = Valve(name=name, flow=value, conns=connections)
    g[name_table[name]] = connections
    open_valves[name_table[name]] = False #v.open
    flow[name_table[name]] = v.flow

for gi in g:
    cons = []
    for i in g[gi]:
        cons.append(name_table[i.strip()])
    g[gi] = cons

print()

