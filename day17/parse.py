with open('height-and-rock-idx.txt','r') as fh:
    data = fh.readlines()
data = [
    int(line.split()[0]) for line in data
]
delta = [
    y-x for x, y in zip(data[::5], data[5::5])
]


print()