from collections import defaultdict
from functools import cache
from time import perf_counter
import igraph as ig
import matplotlib.pyplot as plt

with open('input.txt', 'r') as fh:
    data = fh.readlines()

valves = defaultdict(tuple)
name_table = defaultdict(int)

i = 0
for line in data:
    sp = line.split()
    name = sp[1].strip()
    flow = int(sp[4][5:-1]) # after eq sign to last integer char
    conns = [a.replace(',', '') for a in sp[9:]]
    
    valves[name] = (flow, conns)
    name_table[name] = i
    i+=1

n_vert = len(valves)
edges =[]
for key, values in valves.items():
    for value in values[1]:
        connection = (name_table[name], name_table[value])
        edges.append(connection)

g = ig.Graph(n_vert, edges)
g.vs["name"] = [valves.keys()]
fig, ax = plt.subplots(figsize=(5,5))
ig.plot(
    g,
    target=ax,
    layout="circle", # print nodes in a circular layout
    vertex_size=0.1)
plt.show()