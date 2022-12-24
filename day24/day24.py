from collections import defaultdict
data = open('test.txt').readlines()

data = [line.strip() for line in data]

idx_a = [i for i, val in enumerate(data[0]) if val == '.'][0]
idx_b = [i for i, val in enumerate(data[-1]) if val == '.'][0]

dir_chr = {'<': -1+0j, '>': 1+0j, '^': -1j, 'V': 1j}
bliz = set()
max_y = len(data) - 2 
min_y = 1
min_x = 1
max_x = len(data[0]) - 2
ENTRANCE = complex(idx_a, 0)
curr = ENTRANCE
EXIT = complex(idx_b, len(data) - 1)

def print_grid(x, y, bliz: list):
    for yi in range(y+2):
        for xi in  range(x+2):
            if xi == 0 or xi == x+1 or yi == 0 or yi == y+1:
                if complex(xi, yi) == ENTRANCE or complex(xi,yi) == EXIT:
                    print('E', end='')
                else:
                    print('#',end='')
            elif complex(xi, yi) in [b.position for b in bliz]:
                b = [obj for obj in bliz if obj.position == complex(xi, yi)][0]
                key = [key for key, val in dir_chr.items() if val == b.direction][0]
                print(key, end='')
            else:
                print('.', end='')
        print()
class Bliz:
    def __init__(self, direction: complex, pos: complex) -> None:
        self.direction = direction
        self.position = pos
    
    def move(self):
        self.position += self.direction
        if self.position.imag > max_y:
            self.position = complex(
                self.position.real,
                min_y
            )
        if self.position.imag < min_y:
            self.position = complex(
                self.position.real,
                max_y
            )
        if self.position.real > max_x:
            self.position = complex(
                min_x,
                self.position.imag
            )
        if self.position.real < min_x:
            self.position = complex(
                max_x,
                self.position.imag
            )

for y, line in enumerate(data):
    for x, ch in enumerate(line):
        if ch in dir_chr.keys():
            direction = dir_chr[ch]
            pos = complex(x, y)
            b = Bliz(direction, pos)
            bliz.add(b)

#print_grid(max_x, max_y, bliz)
for b in bliz:
    b.move()

mins = 0
while curr != EXIT:
    # move or wait
    pass