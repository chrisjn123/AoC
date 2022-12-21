from collections import defaultdict
from itertools import cycle
import os
import  copy
from time import sleep, perf_counter
from functools import cache
import os

HEIGHT = 3
COMPLETED_POINTS = set()
stopped = 0
def printRock(rock):
    val = int(max([i.imag for i in rock]))
    low = val - 40 if val - 40 > -1 else -1
    for y in range(1 + val, low, -1):
        for x in range(-1, 8):
            if x == -1 or x == 7:
                print('|', end='')
            elif complex(x, y) in rock:
                print('@', end='')
            elif complex(x, y) in COMPLETED_POINTS:
                print('#', end='')
            else:
                print('.', end='')
        print()

def can_move_x(rock, dx) -> bool:
    ret = True
    for coord in rock:
        if coord + dx in COMPLETED_POINTS:
            ret = False
            return ret
    min_x = int(min([x.real for x in rock]))
    max_x = int(max([x.real for x in rock]))
    if min_x == 0 or max_x >= 6:
        if min_x == 0 and dx > 0:
            ret = True
        elif max_x == 6 and dx < 0:
            ret = True
        else:
            ret = False
    return ret

def can_move_y(rock) -> bool:
    ret = True
    if int(min([a.imag for a in rock])) == 0:
        ret =  False
    else:
        for coord in rock:
            if (coord - 1j) in COMPLETED_POINTS:
                ret = False
                break
    return ret


def find_completed_rows(points: set, rock) :
    rock_y = {val.imag for val in rock}
    for y in rock_y:
        completed = True
        for x in range(0, 7):
            completed = completed and complex(x, y) in points
        if completed:
            for val in frozenset(points):
                if val.imag < y:
                    points.remove(val)
            return
    return 


def  update_height_of_rock(rock):
    for i, coord in enumerate(rock):
        coord += complex(0, HEIGHT)
        rock[i] = coord
    return rock

def main():
    global HEIGHT, stopped
    with open('input.txt', 'r') as fh:
        jet = [ch for ch in fh.readlines()[0].strip()]
    jet = cycle([1 if ch == '>' else -1 for ch in jet])

    rocks = cycle([
        [2+0j, 3+0j, 4+0j, 5+0j], # line horizontal
        [3+0j, 2 + 1j, 3+1j, 4+1j, 3+2j], # plus
        [2+0j, 3+0j, 4+0j, 4+1j, 4+2j], # L shape (reversed)
        [2+0j, 2+1j, 2+2j, 2+3j], # line vertical
        [2+0j, 3+0j, 2+1j, 3+1j], # square
    ])

    '''while True:
        os.system('cls')
        rock = next(rocks)
        printRock(rock)
        sleep(0.5)'''

    rock_idx = 0
    rock = copy.copy(next(rocks))
    rock = update_height_of_rock(rock)
    op = 1
    # main loop
    while stopped < 100_000:
        '''os.system('cls')
        printRock(rock)
        print('+-------+')
        print()'''
        if op == 0:
            # if it can move down
            if can_move_y(rock):
                for i, _ in enumerate(rock):
                    rock[i] -= 1j
            # otherwise its done, so generate new rock
            else:
                for coord in rock:
                    COMPLETED_POINTS.add(coord)
                #print(f'Size of all points BEFORE: {len(COMPLETED_POINTS)}')
                find_completed_rows(COMPLETED_POINTS, rock)
                #print(f'Size of all points AFTER : {len(COMPLETED_POINTS)}')
                with open('height-and-rock-idx.txt', 'a+') as fh:
                    fh.write(f'{HEIGHT}\t{rock_idx}\n')
                rock_idx = 0 if rock_idx + 1 == 5 else rock_idx + 1

                HEIGHT = max(
                    HEIGHT,
                    int(max([a.imag for a in rock])) + 4
                )
                
                rock = copy.copy(next(rocks))
                rock = update_height_of_rock(rock)
                stopped += 1
                
            op = 1
        elif op == 1:
            x_dir = next(jet)
            # if can move left or right
            #print(f'Checking X {x_dir}...',end='')
            if can_move_x(rock, x_dir):
                #print('yes')
                for i, coord in enumerate(rock):
                    rock[i] += x_dir
            else:
                #print('no')
                pass

            op = 0
        #sleep(0.005)
        
    print(stopped, end='\t')
    print(sorted([a.imag for a in COMPLETED_POINTS])[-1] + 1)

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    main()
    print(f'TIme: {1000 *(perf_counter() - start)} ms')
