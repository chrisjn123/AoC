with open('input.txt', 'r') as fh:
#with open('test.txt', 'r') as fh:
    data = [line for line in fh.readlines()]

for ln, line in enumerate(data):
    if '[' in line:
        continue
    else:
        maxStacks = int(line.split()[-1])
        a = ln + 2
        break
moves = data[a:]
stackData = data[:a-2]

stacks = {
    i : [] for i in range(1, maxStacks + 1)
}

for line in stackData:
    sp = line.split()
    for idx, item in enumerate(sp):
        if item == '[0]':
            continue
        else:
            stacks[idx +1].append(item.replace(']', '').replace('[', ''))

for key in stacks.keys():
    stacks[key] = stacks[key][::-1]
    #print('\n'.join(stacks[key]))
    
for line in moves:
    sp = line.split('from')
    quant = int(sp[0].replace('move ', ''))
    src = int(sp[1].split('to')[0])
    dest = int(sp[1].split('to')[1])
    #print(f'{quant}\t{src}\t{dest}')

    idx_end = len(stacks[src]) - 1
    toAdd = stacks[src][idx_end - quant + 1:] 
    for item in toAdd:
        stacks[dest].append(item)
    stacks[src] = stacks[src][:idx_end - quant + 1]

    #for i in range(0,quant):
    #    stacks[dest].append(stacks[src][-1])
    #    stacks[src] = stacks[src][:-1]

for key in stacks.keys():
    print(stacks[key][-1], end='')
    # print('Last elem of {}:\t{}'.format(key, stacks[key][-1]))
print()