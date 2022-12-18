from collections import deque
from time import perf_counter

data = [line.strip() for line in open('input.txt').readlines()]

points = set()
for line in data:
    x, y, z = line.split(',')
    x, y, z = int(x), int(y), int(z)

    points.add((x, y, z))

def findAdjacent(point):
    x, y, z = point
    return [
        (x+1, y, z),
        (x-1, y, z),
        (x, y+1, z),
        (x, y-1, z),
        (x, y, z+1),
        (x, y, z-1)
    ]

CUBE_OUT = set()
CUBE_IN = set()

import functools
@functools.cache
def BFS(point: tuple):
    x, y, z = point
    if point in CUBE_OUT:
        return True
    if point in CUBE_IN: 
        return False
    visited = set()
    q = deque([point])
    while q:
        x, y, z = q.popleft() # get from queue
        # if the point is already processed or is listed in the pts set
        if (x, y, z) in points or (x, y, z) in visited:
            continue
        # Add current to the visited set
        visited.add((x, y, z))
        if len(visited) > 5000:
            for visit in visited:
                CUBE_OUT.add(visit)
            return True
        adj_pts = findAdjacent((x, y, z))
        # add adj pts to queue
        for pt in adj_pts:
            xi, yi, zi = pt
            q.append((xi, yi, zi))
    for pt in visited:
        CUBE_IN.add(pt)
    return False

start = perf_counter()
surf_area = 0
for point in points:
    x, y, z, = point

    if BFS((x+1, y, z)):
        surf_area +=1
    if BFS((x-1, y, z)):
        surf_area +=1
    if BFS((x, y+1, z)):
        surf_area +=1
    if BFS((x, y-1, z)):
        surf_area +=1
    if BFS((x, y, z+1)):
        surf_area +=1
    if BFS((x, y, z-1)):
        surf_area +=1
print(surf_area)

print(f'Time: {1000 * (perf_counter() - start)} ms ')