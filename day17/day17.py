from collections import defaultdict
from itertools import cycle
import os
import  copy

HEIGHT = 3
COMPLETED_POINTS = set()
stopped = 0
def printRock(rock):
    val = int(max([i.imag for i in rock]))
    for y in range(1 + val, -1, -1):
        for x in range(0, 7):
            if complex(x, y) in rock:
                print('@', end='')
            elif complex(x, y) in COMPLETED_POINTS:
                print('#', end='')
            else:
                print('.', end='')
        print()

def can_move_x(rock, dx) -> bool:
    ret = True
    for coord in rock:
        if coord - 1 in COMPLETED_POINTS:
            ret = False
            break
    min_x = int(min([x.real for x in rock]))
    max_x = int(max([x.real for x in rock]))
    if min_x == 0 or max_x >= 6:
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

def  update_height_of_rock(rock):
    for i, coord in enumerate(rock):
        coord += complex(0, HEIGHT)
        rock[i] = coord
    return rock

def main():
    global HEIGHT, stopped
    with open('test.txt', 'r') as fh:
        jet = [ch for ch in fh.readlines()[0]]
    jet = cycle([1 if ch == '>' else -1 for ch in jet])

    rocks = cycle([
        [2+0j, 3+0j, 4+0j, 5+0j], # line horizontal
        [3+0j, 2 + 1j, 3+1j, 4+1j, 3+2j], # plus
        [4+0j, 4+1j, 2+2j, 3+2j, 4+2j], # L shape (reversed)
        [2+0j, 2+1j, 2+2j, 2+3j], # line vertical
        [2+0j, 3+0j, 2+1j, 3+1j], # square
    ])

    rock = copy.copy(next(rocks))
    rock = update_height_of_rock(rock)

    # main loop
    while stopped < 2022:
        x_dir = next(jet)
        
        # if can move left or right
        if can_move_x(rock, x_dir) and can_move_y(rock):
            for i, coord in enumerate(rock):
                rock[i] += x_dir
        # if it can move down
        if can_move_y(rock):
            for i, _ in enumerate(rock):
                rock[i] -= 1j
        # otherwise its done, so generate new rock
        else:
            for coord in rock:
                COMPLETED_POINTS.add(coord)
            HEIGHT = int(max([a.imag for a in COMPLETED_POINTS])) + 3
            rock = copy.copy(next(rocks))
            rock = update_height_of_rock(rock)
            stopped += 1
        '''os.system('cls')
        printRock(rock)
        print('='*7)
        print()'''
    print()


    

if __name__ == '__main__':
    main()