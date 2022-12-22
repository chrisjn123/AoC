from collections import defaultdict
import sys

lines = open('input.txt').readlines()
maths = defaultdict()

for line in lines:
    key, value = line.split(': ')
    key=key.strip()
    value=value.strip()

    maths[key]= value

def find_answer(key='root'):
    op = maths[key]
    try:
        tmp = int(op)
        return tmp
    except:
        sp = op.split()
        if key == 'root':
            sp = [sp[0], '==', sp[2]]
        return int(eval(f'{find_answer(sp[0])}{sp[1]}{find_answer(sp[2])}'))

high = sys.maxsize
low = 0

left, _, right = maths['root'].split()

maths['humn'] = 1
test_neg = (find_answer(left) - find_answer(right)) > 0

while True:
    maths['humn'] = (low + high) // 2
    print(f'Checking {maths["humn"]}...')
    a = find_answer(left)
    b = find_answer(right)   
    print(f'{a}\t{b}') 
    if maths['humn'] == low:
        print('end reached...')
        break
    if a > b:
        if test_neg:
            low = maths['humn']
        else:
            high = maths['humn']
    elif b > a:
        if test_neg:
            high = maths['humn']
        else:
            low = maths['humn']
    else:
        print(f"Found: {maths['humn']}")
        break