from collections import defaultdict
data = [line.strip() for line in open('input.txt').readlines()]

X = 1
cycles = 1

c2v = defaultdict(int)
c2v[0] = 1
for ins in data:
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
        cycles += 1
        X = X + val
        c2v[cycles] = X
    
    

s = 0
for i in [20, 60, 100, 140, 180, 220]:
    s += (c2v[i] * i)
    print(c2v[i] * i)
print(s)
'''
c2i = defaultdict(str)
cycles = 1
for line in data:
    if 'noop' == line:
        c2i[cycles] = line
        cycles += 1
    else:
        c2i[cycles] = line
        cycles += 1
        c2[]


        '''