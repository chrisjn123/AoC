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


row_test = 2000000
grid = set()
for sensor, beacon in sen_beac.items():
    distance = manhattan(sensor, beacon)
    distance_to_y = abs(sensor[1] - row_test)
    width = distance - distance_to_y

    if width > 0:
        for x in range(sensor[0] - width, sensor[0] + width):
            if (x, row_test) not in sen_beac.values():
                grid.add((x, row_test))
            else:
                pass

len_y_row = len(grid)

end = perf_counter()
print(f'Time: {round(1000* (end-start), 2)} ms')
print(f'Length: {len_y_row}')
