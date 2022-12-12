from collections import defaultdict
from queue import PriorityQueue
import time

#data = [line.strip() for line in open('test.txt').readlines()]
data = [line.strip() for line in open('input.txt').readlines()]
to_nums = {chr(i) : i - 96 for i in range(97, 123)}
to_nums['E'] = 26
to_nums['S'] = 1
grid = []

for i, line in enumerate(data):
    for j,  _ in enumerate(line):
        grid.append((i, j))

def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2

    return abs(x1-x2) + abs(y1-y2)

map = defaultdict(dict)

st = None
ed = None
starts = list()

for cell in grid:
    i, j = cell

    if data[i][j] == 'E':
        ed = cell
    elif data[i][j] == 'S':
        st = cell
        starts.append(cell)
    elif data[i][j] == 'a':
        starts.append(cell)
    
    dirs = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
    check_north = True
    check_south = True
    check_east = True
    check_west = True

    if i == 0: 
        check_north = False
    elif i == len(data) - 1:
        check_south = False
    
    if j == 0:
        check_west = False
    elif j == len(data[0]) - 1:
        check_east = False

    if check_north and (to_nums[data[i][j]] >= to_nums[data[i - 1][j]] or (to_nums[data[i][j]] - to_nums[data[i - 1][j]]) == -1 ):
        dirs['N'] = 1
    if check_south and (to_nums[data[i][j]] >= to_nums[data[i + 1][j]] or (to_nums[data[i][j]] - to_nums[data[i + 1][j]]) == -1 ):
        dirs['S'] = 1
    if check_east and (to_nums[data[i][j]] >= to_nums[data[i][j + 1]] or (to_nums[data[i][j]] - to_nums[data[i][j + 1]]) == -1 ):
        dirs['E'] = 1
    if check_west and (to_nums[data[i][j]] >= to_nums[data[i][j - 1]] or (to_nums[data[i][j]] - to_nums[data[i][j - 1]]) == -1 ):
        dirs['W'] = 1
    
    map[cell] = dirs 

def aStar():
    global st, ed
    start = st
    g_score={cell:float('inf') for cell in grid}
    g_score[start] = 0
    f_score={cell:float('inf') for cell in grid}
    f_score[start] = h(start, ed)

    open=PriorityQueue()
    open.put((h(start, ed), h(start, ed), start))
    aPath={}
    while not open.empty():
        currCell=open.get()[2]
        if currCell == ed:
            break
        for d in 'ESNW':
            if map[currCell][d] == True:
                match d:
                    case 'E':
                        childCell=(currCell[0],currCell[1] + 1)
                    case 'W':
                        childCell=(currCell[0],currCell[1] - 1)
                    case 'N':
                        childCell=(currCell[0] - 1,currCell[1])
                    case 'S':
                        childCell=(currCell[0] + 1,currCell[1])

                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell, ed)

                if temp_f_score < f_score[childCell]:
                    g_score[childCell]= temp_g_score
                    f_score[childCell]= temp_f_score
                    open.put((temp_f_score, h(childCell, ed), childCell))
                    aPath[childCell] = currCell
    fwdPath={}
    cell = ed
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    return fwdPath

pathes = []
for i, start in enumerate(starts):
    st = start
    #print(f'Running elevation a #{i+1} ({round(100 * (i+1) / len(starts), 2)}%)')
    try:
        path=aStar()
        pathes.append(len(path))
    except KeyError:
        continue
print(f'Minimum: {min(pathes)}')
