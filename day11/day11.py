from collections import defaultdict

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
        
    
    def test(self) -> list:
        # Test: divisible by 7
        out = []
        for val in self.starting_items:
            test_op = self.test_string.split()[0]
            test_val = int(self.test_string.split()[-1])

            match test_op:
                case 'divisible':
                    if val % test_val == 0:
                        out.append(int(self.res[0].split()[-1]))
                    else:
                        out.append(int(self.res[1].split()[-1]))
                case _:
                    pass
        return out

    def operation(self):
        op = self.op.split('=')[-1]
        left = op.split()[0]
        operator_ch = op.split()[1]
        right = op.split()[2]

        if left == right:
            same = True
        else:
            same = False

        for i, _ in enumerate(self.starting_items):
            self.inspection_count += 1
            match operator_ch:
                case '*':
                    if same:
                        self.starting_items[i] *= self.starting_items[i]
                    else:
                        self.starting_items[i] *= int(right)
                case '-':
                    if same:
                        self.starting_items[i] -= self.starting_items[i]
                    else:
                        self.starting_items[i] -= int(right)
                case '+':
                    if same:
                        self.starting_items[i] += self.starting_items[i]
                    else:
                        self.starting_items[i] += int(right)
                case '/':
                    if same:
                        self.starting_items[i] /= self.starting_items[i]
                    else:
                        self.starting_items[i] /= int(right)
            #self.starting_items[i] = self.starting_items[i] // 3
        
for monkey in data:
    id = int(monkey[0].split()[-1].replace(':', ''))
    items = monkey[1].split(':')[-1].split(',')
    op = monkey[2].split(":")[-1]
    test = monkey[3].split(':')[-1]
    t_case = monkey[4].split(':')[-1]
    f_case = monkey[5].split(':')[-1]

    monkies[id] = Monkey(id=id, starting=items, op=op, test=test, test_res=[t_case, f_case])

# 20 rounds
for i in range(1, 10000 +1):
    print(f'Running round {i}')
    # Runs 1 Round
    for monkey_id in monkies.keys():
        monkies[monkey_id].operation()
        to_monkies = monkies[monkey_id].test()
        for i, dest in enumerate(to_monkies):
            monkies[dest].starting_items.append(
                monkies[monkey_id].starting_items[i]
            )
        monkies[monkey_id].starting_items.clear()

id_count = {monkies[monkey].id : monkies[monkey].inspection_count for monkey in monkies}
print()