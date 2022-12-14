from time import perf_counter
from collections import defaultdict
from colorama import Fore


def blocked(sands) -> bool:
    ret = False
    if (499, 1) in sands and (500, 1) and (501, 1) in sands:
        ret = True

    return ret

def void(x, y, grid, sands) -> bool:
    column = {key: value 
        for key, value in grid.items() 
        if key[0] == x and y < key[1] }
    for sand in sands:
        xS, yS = sand
        if xS == x and yS > y:
            column[sand] = 'o'
    if '#' in column.values() or 'o' in column.values():
        return False
    return True
    

def main() -> None:
    with open('input.txt', 'r') as fh:
        data = [line for line in fh.readlines()]
    
    grid = defaultdict(str)
    grid[(500, 0)] = '+'
    for line in data:
        rock_lines = [(int(pair.split(',')[0]),
            int(pair.split(',')[-1])) 
            for pair in line.split('->')]
        
        for i in range(len(rock_lines) -1):
            x1, y1 = rock_lines[i]
            x2, y2 = rock_lines[i+1]

            if x1 == x2:
                if y1 > y2:
                    y1, y2 = y2, y1
                for y in range(y1, y2 + 1):
                    grid[(x1, y)] = '#'
            elif y1 == y2:
                if x1 > x2:
                    x1, x2 = x2, x1
                for x in range(x1, x2 + 1):
                    grid[(x, y1)] = '#'
            else:
                print(rock_lines[i])

    
    # Process sand
    sands = set((500, 0))
    #idx = 0
    
    min_x = min([pair[0] for pair in grid.keys()]) - 2
    max_x = max([pair[0] for pair in grid.keys()]) + 2
    min_y = 0
    max_y = max([pair[-1] for pair in grid.keys()]) + 2

    for x in range(min_x -100000, max_x + 100000 + 1):
        grid[(x,max_y)] = '#'

    '''for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            pair = (x, y)
            if grid[pair] != '#' and grid[pair] != '+':
                if pair in sands:
                    print('o', end='')
                else:
                    print('.', end='')
            else:
                print(grid[pair], end='')
        print()
    count = input('continue? ')
    if count == 'n':
        return'''

    currSand = (500,0)
    while True:
        #print(f'There are [{len(sands) - 1}] sand particles at rest.')
        x, y = currSand
        # if cell below me is available (i.e. not sand or rock)
        if grid[(x, y+1)] != '#' and (x, y+1) not in sands:
            isVoid = blocked(sands)
            currSand = (x, y+1)
        # elif, diag left is available
        elif grid[(x-1, y+1)] != '#' and (x-1, y+1) not in sands:
            currSand = (x-1, y+1)
        # elif, diag right is available
        elif grid[(x+1, y+1)] != '#' and (x+1, y+1) not in sands:
            currSand = (x+1, y+1)
        # elif directly below is a sand or rock
        elif (x, y+1) in grid.keys() or (x, y+1) in sands:
            #print(f'There are [{len(sands)}] sand particles at rest.')
            #idx += 1
            #sands.append((500, 0))
            sands.add(currSand)
            currSand = (500, 0)
            if blocked(sands):
                print(f'Blocked State Reached: {len(sands)}')
                break
        # if void found, break
        if isVoid:
            sands.pop()
            print(f'Blocked State Reached: {len(sands)}')
            break

    max_y = max([pair[-1] for pair in grid.keys()]) 
    min_x = min([pair[0] for pair in grid.keys()if pair[-1] <= max_y and pair[0] > 325]) 
    max_x = max([pair[0] for pair in grid.keys() if pair[-1] <= max_y and pair[0] < 700]) 
    min_y = 0

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



if __name__ == "__main__":
    start_time = perf_counter()
    main()
    end_time = perf_counter()
    print(f'Time: {round((end_time - start_time) * 1000, 2)} ms')