from collections import defaultdict
TEST = False

if TEST:
    data = [line.strip() for line in open('test.txt').readlines()]
else: 
    data = [line.strip() for line in open('input.txt').readlines()]

# day 9
'''
visited = 0
tracked = defaultdict(int)

h_loc = {'x': 0, 'y': 0} 
t_loc = {'x': 0, 'y': 0} 

def closeToH():
    #if h_loc['x'] in [t_loc['x'] - 1, t_loc['x'] + 1, t_loc['x']] \
    #    and t_loc['y']  in [t_loc['y'] - 1, t_loc['y'] + 1, t_loc['y']]:
    #   return True

    if abs(h_loc['x'] - t_loc['x']) >= 2 or abs(h_loc['y'] - t_loc['y']) >= 2:
        return False
    return True

def diag():
    if h_loc['x'] != t_loc['x'] and h_loc['y'] != t_loc['y']:
        return True
    return False

def move_diag():
    if h_loc['x'] > t_loc['x']:
        t_loc['x'] += 1
    else:
        t_loc['x'] -= 1
    
    if h_loc['y'] > t_loc['y']:
        t_loc['y'] += 1
    else:
        t_loc['y'] -= 1
    
def move(direction: str, amount: int):
    delta = 1
    global h_loc, t_loc, visited
    if direction in ['L', 'D']:
        delta = -1
    for _ in range(amount):
        if direction == 'L' or direction == 'R':
            h_loc['x'] += delta
            if not closeToH():
                if not diag():
                    t_loc['x'] += delta
                else:
                    move_diag()
                visited += 1
                tracked[(t_loc['x'], t_loc['y'])] += 1
        else:
            h_loc['y'] += delta
            if not closeToH():
                if not diag():
                    t_loc['y'] += delta
                else:
                    move_diag()
        
                visited += 1
                tracked[(t_loc['x'], t_loc['y'])] += 1

for line in data:
    move(
        line.split()[0],
        int(line.split()[-1])
    )
print(f'Visited: {len(tracked)}')
'''

# Part 2

def generic_move(direction:str, position:int) -> tuple:
    if direction == 'R':
        tmp = (position[0] + 1, position[1])
    elif direction == 'L':
        tmp = (position[0] - 1, position[1])
    elif direction == 'D':
        tmp = (position[0], position[1] - 1)
    else:
        tmp = (position[0], position[1] + 1)
    return tmp

def needs_to_move(h_x, h_y, t_x, t_y) -> bool:
    return abs(t_x - h_x) > 1 or abs(t_y - h_y) > 1

def array_move_tail(current_head, target_tail) -> tuple:
    t_x, t_y = target_tail
    h_x, h_y = current_head
    next_tail = target_tail

    if needs_to_move(h_x, h_y, t_x, t_y):
        if h_x < t_x:
            next_tail = generic_move('L', next_tail)
        else:
            next_tail = generic_move('L', next_tail)

        if h_y < t_y:
            next_tail = generic_move('D', next_tail)
        else:
            next_tail = generic_move('U', next_tail)
        
        return next_tail
    else:
        return target_tail  
    

def run(moves: list, num_knots=1):
    s = (0,0)
    tracked_points = set([s])

    head = s
    tail = [s for _ in range(num_knots)]

    for move in moves:
        direction, quant = move.split()

        for _ in range(int(quant)):
            head = generic_move(direction, head)

            in_line = head
            for i, tl in enumerate(tail):
                tail[i] = array_move_tail(in_line, tl)
                in_line = tail[i]
            
            tracked_points.add(tail[-1])
    
    return len(tracked_points)

print(run(data, 9))