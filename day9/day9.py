TEST = False

if TEST:
    data = [line.strip() for line in open('test.txt').readlines()]
else: 
    data = [line.strip() for line in open('input.txt').readlines()]

# day 9
visited = 0

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
        else:
            h_loc['y'] += delta
            if not closeToH():
                if not diag():
                    t_loc['y'] += delta
                else:
                    move_diag()
        
                visited += 1
    #print(f'H: {h_loc["x"]}, {h_loc["y"]}')
    #print(f'T: {t_loc["x"]}, {t_loc["y"]}')
    #print('------------------')

for line in data:
    move(
        line.split()[0],
        int(line.split()[-1])
    )
print(f'Visitied: {visited}')