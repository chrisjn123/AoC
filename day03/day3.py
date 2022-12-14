#with open('test.txt', 'r') as fh:
with open('input.txt', 'r') as fh:
    lines = [
        line.strip() for line in fh.readlines()
    ]

priorities = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

rucksacks = []
for line in lines:
    half = len(line) // 2
    h1 = line[0:half]
    h2 = line[half:]
    rucksacks.append([h1, h2])

triples = [lines[i:i+3] for i in range(0, len(lines),3)]

total = 0
for pair in rucksacks:
    print()
    s1 = sorted(set(pair[0]))
    s2 = sorted(set(pair[1]))

    done = False
    for ch in s1:
        for ch2 in s2:
            if ch == ch2:
                total += priorities[ch.lower()]
                upper = 0
                if ch in [i.upper() for i in priorities.keys()]:
                    upper = 1
                    total += 26
                done == True
                break
        if done:
            break
print(total)

total = 0
for tri in triples:
    done = False
    for ch1 in set(tri[0]):
        for ch2 in set(tri[1]):
            if ch1 != ch2:
                continue
            for ch3 in set(tri[2]):
                if ch1 == ch2 == ch3:
                    total += priorities[ch1.lower()]
                    if ch1 in [i.upper() for i in priorities.keys()]:
                        total += 26
                        done =True
                    break
        if done:
            break
print(total)