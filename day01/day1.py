import numpy as np

with open('input.txt', 'r') as fh:
    data = [i.strip() for i in fh.readlines()]

i = 0
cnt = len([i for i in data if i ==''])
elves = {x: 0 for x in range(cnt + 1)}
for line in data:
    if (line == ''):
        i+=1
        continue
    elves[i] += int(line)

# Part 1
maxE = max(elves.values())
print(maxE)

# part 2
maxE = sorted(elves.values())
print(sum(maxE[-3:]))