from functools import cmp_to_key
from time import perf_counter
from copy import copy, deepcopy
from collections import defaultdict
from colorama import Fore


def void(x, y, grid) -> bool:
    column = {key: value 
        for key, value in grid.items() 
        if key[0] == x and y < key[1]}
    if '#' in column.values():
        return False
    return True
    

def main() -> None:
    with open('input.txt', 'r') as fh:
        data = [line for line in fh.readlines()]

    
    sand_at_rest = 0
    grid = defaultdict(str)
    grid[(500, 0)] = '+'
    for line in data:
        rock_lines = [(int(pair.split(',')[0]), int(pair.split(',')[-1])) for pair in line.split('->')]
        
        for i in range(len(rock_lines) -1):
            x1, y1 = rock_lines[i]
            x2, y2 = rock_lines[i+1]

            if x1 == x2:
                if y1 > y2:
                    y1, x2 = y2, y1
                for y in range(y1, y2 + 1):
                    grid[(x1, y)] = '#'
            elif y1 == y2:
                if x1 > x2:
                    x1, x2 = x2, x1
                for x in range(x1, x2 + 1):
                    grid[(x, y1)] = '#'

    
    # Process sand
    sands = [(500, 0)]
    idx = 0
    count = ''

    min_x = min([pair[0] for pair in grid.keys()]) - 2
    max_x = max([pair[0] for pair in grid.keys()]) + 2
    min_y = 0
    max_y = max([pair[-1] for pair in grid.keys()]) + 2


    while True:
        #print(f'There are [{len(sands) - 1}] sand particles at rest.')
        x, y = sands[idx]
        # if cell below me is available (i.e. not sand or rock)
        if  grid[(x, y+1)] != '#' and (x, y+1) not in sands:
            sands[idx] = (x, y+1)
            isVoid = void(x, y, grid)
        # elif, diag left is available
        elif grid[(x-1, y+1)] != '#' and (x-1, y+1) not in sands:
            sands[idx] = (x-1, y+1)
        # elif, diag right is available
        elif grid[(x+1, y+1)] != '#' and (x+1, y+1) not in sands:
            sands[idx] = (x+1, y+1)
        # elif directly below is a sand or rock
        elif (x, y+1) in grid.keys() or (x, y+1) in sands:
            print(f'There are [{len(sands)}] sand particles at rest.')
            idx += 1
            sands.append((500, 0))
        # if void found, break
        if isVoid:
            sands.pop(-1)
            print(f'Void Reached: {len(sands)}')
            break


        if len(sands) -1 == 627 and False:
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    pair = (x, y)
                    if grid[pair] != '#' and grid[pair] != '+':
                        if pair in sands:
                            print(Fore.GREEN + 'o' + Fore.RESET, end='')
                        else:
                            print('.', end='')
                    else:
                        print(Fore.YELLOW + grid[pair] + Fore.RESET, end='')
                print()
            count = input('continue? ')
            if count == 'n':
                return


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    end_time = perf_counter()
    print(f'Time: {round((end_time - start_time) * 1000, 2)} ms')