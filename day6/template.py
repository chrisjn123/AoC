#with open('test.txt', 'r') as fh:
with open('input.txt', 'r') as fh:
    data = [line.strip() for line in fh.readlines()]

# start of day 6
data=data[0]

def count_unique(chars: str) -> bool:
    c = {ch : 0 for ch in chars}

    for ch in chars:
        c[ch] += 1
        if c[ch] > 1:
            return False
    return True

def get_list(data:list, number: int) -> list:
    return [data[i:i+number] for i in range(0, len(data)-number)]

#for i, char_set in enumerate(get_list(data, 4)):
for i, char_set in enumerate(get_list(data, 14)):
    if count_unique(char_set):
        print(data.index(char_set) + len(char_set))
        print(char_set)
        break