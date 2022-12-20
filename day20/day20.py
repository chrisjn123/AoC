from collections import deque
from time import perf_counter

def get_answer(line: list) -> int:
    line = [x for x, _ in line]
    idx_of_Z = line.index(0)
    return (
        line[(1000 + idx_of_Z) % len(line)] +
        line[(2000 + idx_of_Z) % len(line)] +
        line[(3000 + idx_of_Z) % len(line)]
    )

def main():
    with open('input.txt') as f:
        data = [int(line) * 811589153 for line in f.readlines()]
    
    d = deque()
    for index, val in enumerate(data):
        d.append(
            # using the index to make a unique entry
            (val, index)
        )
    # there could be some optomization in the use of 
    # rotate_by  = val % len(data) But I couldn't get it working
    for _ in range(10):    
        for i, val in enumerate(data):
            # move the target number to pos 0
            d.rotate(
                -d.index((val, i))  # search for val and index combo
            )
            d.popleft()             # remove it 
            d.rotate(-val)          # rotate by value (start (0) will be the position to insert)
            d.appendleft((val, i))  # Add it to index 0

    # data is in correct order but rotated out from the ideal postion due to rotates
    # good thing we are using the 0 val as the 0 index
    print(get_answer(list(d)))

if __name__ == '__main__':
    start = perf_counter()
    main()
    print(f'Time: {(perf_counter() - start) * 1000} ms')
