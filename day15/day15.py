import sys
from collections import defaultdict
from time import perf_counter
from  colorama import Fore

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
        for x in range(sensor[0] - width, sensor[0] + width +1):
            if (x, row_test) not in sen_beac.values():
                grid.add((x, row_test))
            else:
                pass

len_y_row = len(grid)

end = perf_counter()
print('~~~~~~~~~~~~~~~~ Part 1 ~~~~~~~~~~~~~~~~')
t = round(1000* (end-start), 2)
print(f'Time: {t} ms')
print(f'{Fore.GREEN}Length: {len_y_row}{Fore.RESET}')

start = perf_counter()
print('~~~~~~~~~~~~~~~~ Part 2 ~~~~~~~~~~~~~~~~')
const_provided = 4_000_000
for sen, dist in sen_man.items():
    leave = False
    for val in range(dist + 1):
        coords = (
            # This makes sense on paper. 
            (sen[0] - dist -1 + val, sen[1] - val),
            (sen[0] + dist + 1 - val, sen[1] - val),
            (sen[0] - dist -1 + val, sen[1] + val),
            (sen[0] + dist + 1 - val, sen[1] + val)
        )
        
        for x, y in coords:
            # if within the zone, AND
            # the distance from sensors is always greater than the sensor to beacon
            # i.e. out of range for all sensors
            if 0 <= x <= const_provided and 0 <= y <= const_provided \
                and all(manhattan((x,y), s2) > d2 for s2, d2 in sen_man.items()):
                print(f'{Fore.CYAN}{x*const_provided + y}{Fore.RESET}')
                end = perf_counter()
                t2 = round(1000* (end-start), 2)
                print(f'Time: {t2} ms')
                print(f'TOTAL TIME: {t+t2} ms')
                sys.exit()