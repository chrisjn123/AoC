from time import sleep
from colorama import Fore
from collections import defaultdict

data = [line.strip() for line in open('input.txt').readlines()]

X = 1
cycles = 1

c2v = defaultdict(int)
c2v[0] = 1
crt = ['.'] * 240
idx = 0
prev = X

def draw():
    global crt, X, cycles, idx
    if X != prev:
        idx = 0
    
    sprite = [X - 1, X, X+1]
    if ((cycles-1)  % 40) in sprite:
        crt[cycles - 1] = "#"
    idx += 1
    if idx > 2:
        idx = 0    

for ins in data:
    draw()
    if ins == 'noop':
        c2v[cycles] = X
        cycles += 1
    else:
        val = int(ins.split()[-1])
        # cycle 1
        c2v[cycles] = X
        cycles += 1
        
        # cycle 2
        c2v[cycles] = X
        draw()
        cycles += 1
        prev = X
        X = X + val
        c2v[cycles] = X
        draw()
    
rows = [crt[i:i+40] for i in range(len(crt), 40) ]

s = 0
for i in [20, 60, 100, 140, 180, 220]:
    s += (c2v[i] * i)
    print(c2v[i] * i)
print(s)
print()

colors = [Fore.CYAN, Fore.RED, Fore.GREEN, Fore.MAGENTA,
    Fore.WHITE, Fore.CYAN, Fore.RED,
    Fore.GREEN, Fore.MAGENTA, Fore.WHITE
]
for i in range(0, 240, 40):
    row = crt[i:i+40]
    for j, ch in enumerate(row):
        color = colors[j // 5]
        print(color, end='')
        sleep(0.01)
        if ch == '#':
            print(u"\u2588", end='')
        else:
            print(' ', end='')
    print(Fore.RESET)