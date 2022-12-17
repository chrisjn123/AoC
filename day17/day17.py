from collections import defaultdict
with open('test.txt', 'r') as fh:
    jet = [ch for ch in fh.readlines()[0]]

rocks = []
rocks.append([['#','#', '#', '#']])
rocks.append([
    ['', '#',''],
    ['#', '#','#'],
    ['', '#', '']
])
rocks.append([
    ['', '', '#'],
    ['', '',  '#'],
    ['#', '#', '#']
])
rocks.append([
    ['#'],
    ['#'],
    ['#'],
    ['#']
])
rocks.append([
    ['#', '#'],
    ['#', '#'],
])
rock_occ = set()

def addToSet(stopped):
    lx, ly, lRock = stopped
    for i in range(len(lRock)):
        for j in range(len(lRock[0])):
            if lRock[i][j] == '#':
                rock_occ.add((j + lx, i + ly))
def checkIntersectionX(rx, ry, rock, direction='left') -> bool:
    global rock_occ

    dx = -1 if direction.lower() == 'left' else 1

    fallingCoords = set()
    fx, fy, fRock = rx, ry, rock
    for i in range(len(fRock)):
        for j in range(len(fRock[0])):
            if fRock[i][j] == '#':
                fallingCoords.add((j + fx, i + fy))

    for x,y in fallingCoords:
        if (x+dx, y) in rock_occ:
            return True
    return False

def checkIntersection(falling) -> bool:
    global rock_occ
    #if len(list(stopped_rocks.keys())) < 1:
    #    return True        
    
    fallingCoords = set()
    fx, fy, fRock = falling
    for i in range(len(fRock)):
        for j in range(len(fRock[0])):
            if fRock[i][j] == '#':
                fallingCoords.add((j + fx, i + fy))

    for x,y in fallingCoords:
        if (x, y-1) in rock_occ:
            return True
    return False



width = 7
height = 3
rock_idx = 0
stopped_rocks = defaultdict()
stop_id = 1
rock_stop_limit = 2022
y_limit = 0
lastX, lastY = 0,0
need_new_rock = True
lastRock = None

def visualize(x, y, rType):
    coord = set()
    for i in range(len(rType)):
        for j in range(len(rType[0])):
            if rType[i][j] == '#':
                coord.add((j + x, i + y))
    yMax = [y for _, y in rock_occ]
    if len(yMax) == 0:
        yMax = [0]
    print('---------------')
    for iy in range(0, max(yMax) + 10):
        for ix in range(0, 7):
            if (ix, iy) in coord:
                print('@', end='')
            elif (ix, iy) in rock_occ:
                print('#', end='')
            else:
                print('.', end='')
        print()
    
while jet:
    # jet current jet motion, circularly add to jets list
    jet_now = jet.pop(0)
    jet.append(jet_now)
    
    # if starting new OR I have a stopped rock
    if need_new_rock:
        if lastRock is not None:
            rock_pos = (2 , height + lastRock[1] + y_limit)  
        else:
            rock_pos = (2 , height)  
        rock = rocks[rock_idx]                              # Rock type
        rock_idx += 1                                       # set for next stoppage
        if rock_idx > 4:
            rock_idx = 0
        need_new_rock = False                               # kill new rock init
        rx, ry = rock_pos                                   # extract position
    
    #visualize(rx, ry, rock)
    
    if checkIntersection((rx, ry, rock)) or ry == 0:
        stopped_rocks[stop_id] = (rx, ry, rock)
        need_new_rock = True
        y_limit = y_limit + len(rock) 
        lastRock = (rx, ry, rock)
        addToSet(lastRock)
        print(f'Stop count = {stop_id}\tY: {max(y for _, y in rock_occ)}')
        stop_id += 1
    else:
        ry -= 1
        match jet_now:
            case '<':
                if rx > 0 and not checkIntersectionX(rx, ry, rock):
                    rx -= 1
            case '>':
                if rx + len(rock[0])  < width and not checkIntersectionX(rx, ry, rock, direction='right'):
                    rx += 1
    #visualize(rx, ry, rock)
    if stop_id >= 2022:
        break

print(f'{max(y for _, y in rock_occ)}')

