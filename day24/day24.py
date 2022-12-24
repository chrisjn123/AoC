from collections import defaultdict, deque
import sys

fname = 'input.txt'

data = [
    line.strip() for line in open(fname).readlines()
]

dir_ch = {
    '<': -1+0j,
    '>': 1+0j,
    '^': 0-1j,
    'V': 0+1j
}

# each coord will store the list of blizzard types (directions)
bliz = defaultdict(list)

# I don't want to deal with 1 based index so... align to 0
for y, line in enumerate(data):
    for x, ch in enumerate(line):
        if ch in dir_ch.keys():
            bliz[(x-1) + (y-1)*1j].append(dir_ch[ch])

width = len(data[0]) - 2
height = len(data) - 2
start = -1j
end = height*1j + width-1

def move_bliz(bliz:dict, h:int, w:int):
    new_bliz = defaultdict(list)
    for pos, b in bliz.items():
        for pt in b:
            pos_update = ((pos + pt).real % w ) + (1j * ((pos+ pt).imag % h))
            new_bliz[pos_update].append(pt)
    return new_bliz

def move_e(w:int, h, waypoints, loc:complex):
    valid_moves_for_E = {
        point for point in [loc - 1, loc + 1, loc - 1j, loc + 1j]
        if point in waypoints or (point.real in range(w+1) and point.imag in range(h+1)) 
    }
    return valid_moves_for_E


def BFS(grid:dict, w:int, h:int, start:complex, waypoints):
    grid_dict = {0: grid}
    seen = set()
    q = deque()

    q.append((0, start, waypoints))
    while q:
        tm, pos, wp = q.popleft()

        # if position == end
        if pos == wp[0]:
            wp = wp[1:]
            q.clear()

        # if no more points to travel to
        if not wp:
            return tm

        # if the next tuime is not listed
        if not tm + 1 in grid_dict:
            grid_dict[tm + 1] = move_bliz(grid_dict[tm], height, width)
        
        # for each vlaid move
        for mv in move_e(width, height, waypoints, pos):
            if not mv in grid_dict[tm + 1] and not (tm + 1, mv, wp) in seen:
                seen.add((tm + 1, mv, wp))
                q.append((tm + 1, mv, wp))


print(BFS(bliz, width, height, start, (end,)))
print(BFS(bliz, width, height, start, (end, start, end)))