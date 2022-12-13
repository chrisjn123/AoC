from functools import cmp_to_key

data = open('input.txt').read().split('\n\n')
data_test = open('test.txt').read().split('\n\n')

pairs = []
for line in data:
    p1, p2 = line.split('\n')
    p1 = eval(p1)
    p2 = eval(p2)
    pairs.append([p1,p2])

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right :
            return -1
        elif left == right:
            return 0
        else:
            return 1

    elif isinstance(left, list) and isinstance(right, list):
        counter = 0
        while(counter < len(left) and counter < len(right)):
            ret = compare(left[counter], right[counter])
            if ret == -1:
                return ret
            if ret == 1:
                return ret
            counter += 1
        
        if counter == len(left) and counter < len(right):
            ret = -1
        elif counter == len(right) and counter < len(left):
            ret = 1
        else:
            ret = 0
        return ret

    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    else:
        return compare(left, [right])


total = 0

packets = []
packets.append([[2]])
packets.append([[6]])

for i, pair in enumerate(pairs):
    p1, p2 = pair
    packets.append(p1) # Part 2
    packets.append(p2) # Part 2
    if compare(p1, p2) == -1:
        total += 1+i
print(total)


total_2 = 1
# Sort packets with the key being the return value from the compare function
packets = sorted(packets, 
    key=cmp_to_key(lambda left, 
        right: compare(left, right)
    )
)
for idx, packet in enumerate(packets):
    if packet == [[2]] or packet == [[6]]:
        print(idx+1, end=' ')
        if packet == [[2]]:
            print('* ', end='')
        else:
            print('= ', end='')
        total_2 *= idx+1

print(total_2)