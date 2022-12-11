from collections import defaultdict
import time

data = open('input.txt').read()
data = data.split('\n\n')

data = [line.split('\n') for line in data]

monkies = defaultdict()

class Monkey:
    def __init__(self, id=0, starting=list, op="", test="", test_res=[]) -> None:
        self.id = id
        self.starting_items = [int(i) for i in starting]
        self.op = op
        self.test_string = test
        self.res=test_res

        self.inspection_count = 0

    def operation(self):
        global monkies
        op = self.op.split('=')[-1]
        if 'old * old' in op:
            old2old = True
        else: 
            old2old = False
        
        op = op.replace('old', '')
        test_val = int(self.test_string.split()[-1])

        while self.starting_items:
            self.inspection_count += 1
            item = self.starting_items.pop(0)
            if old2old:
                worry = eval(f'{item} * {item}') % 9699690
            else:
                worry = eval(f'{item} {op}') % 9699690
            
            if worry % test_val == 0:
                monkies[int(self.res[0].split()[-1])].starting_items.append(worry)
            else:
                monkies[int(self.res[1].split()[-1])].starting_items.append(worry)
        
for monkey in data:
    id = int(monkey[0].split()[-1].replace(':', ''))
    items = monkey[1].split(':')[-1].split(',')
    op = monkey[2].split(":")[-1]
    test = monkey[3].split(':')[-1]
    t_case = monkey[4].split(':')[-1]
    f_case = monkey[5].split(':')[-1]

    monkies[id] = Monkey(id=id, starting=items, op=op, test=test, test_res=[t_case, f_case])

start = time.time()
rounds = 10000
for i in range(1,  rounds+1):
    #print(f'Running round {i} of {rounds} ({100*i / rounds}%)')
    for monkey_id in monkies.keys():
        monkies[monkey_id].operation()
stop = time.time()

id_count = {monkies[monkey].id : monkies[monkey].inspection_count for monkey in monkies}
a = sorted(id_count.values(), reverse=True)[:2]
print(a[0] * a[1], end=' ')
print(f'== 15305381442') 

print('Code ran in {} seconds '.format(round(stop-start, 2)))