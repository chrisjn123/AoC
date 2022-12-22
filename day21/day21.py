from collections import defaultdict

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
        return eval(f'{find_answer(sp[0])}{sp[1]}{find_answer(sp[2])}')

print(find_answer())