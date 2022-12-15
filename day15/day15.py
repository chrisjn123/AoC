from collections import defaultdict
from time import perf_counter

start = perf_counter()

data = [line.strip() for line in open('input.txt').readlines()]

def manhattan(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    return abs(x1-x2) + abs(y1-y2)

sen_beac = defaultdict()
sen_man = defaultdict()

for line in data:
    sensor = None
    beacon = None
    sen = line.split(':')[0].replace('Sensor at ', '').strip()
    bec = line.split(':')[1].replace('closest beacon is at', '').strip()

    sensor = (
        int(sen.split(',')[0].replace('x=','').strip()),
        int(sen.split(',')[1].replace('y=','').strip())
    )
    beacon = (
        int(bec.split(',')[0].replace('x=','').strip()),
        int(bec.split(',')[1].replace('y=','').strip())
    )

    sen_beac[sensor] = beacon
    sen_man[sensor] = manhattan(sensor, beacon)


min_x = min(
        min([key[0] for key in sen_beac.keys()]),
        min([value[0] for value in sen_beac.values()])
)

max_x = max(max([key[0] for key in sen_beac.keys()]), 
    max([value[0] for value in sen_beac.values()]))

min_y = min(min([key[1] for key in sen_beac.keys()]),
    min([value[1] for value in sen_beac.values()]))

max_y = max(max([key[1] for key in sen_beac.keys()]),
    max([value[1] for value in sen_beac.values()]))

row_test = 2000000
len_x = max_x - min_x

grid = defaultdict()
#for y in range(min_y, max_y + 1):
for x in range(min_x, max_x + 1):
    if (x, row_test) in grid.keys():
        continue
    for key in sen_man.keys():
        if manhattan(key, (x, row_test)) <= sen_man[key] \
            or sen_beac[key] == (x,row_test) \
            or key == (x,row_test):
            grid[(x,row_test)] = '#'
'''for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        if (x,y) in grid.keys():
            print(grid[(x,y)], end='')
        else:
            print(' ',end='')
    print()'''

y_row = [key for key in grid.keys() if key[-1] == row_test]

end = perf_counter()
print(f'Time: {round(1000* (end-start), 2)} ms')
print(f'Length: {len(y_row)}')
