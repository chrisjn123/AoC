from collections import defaultdict

disk_size = 70000000        # Part 2
needed_size = 30000000      # Part 2

with open('input.txt', 'r') as fh:
    lines = [line.strip() for line in fh.readlines()]

cwd = list()                # CWD is a list of directories; treat like stack
dirs = defaultdict(int)     # Dictorary of every Directory path with size

for line in lines:
    cmd = line.split()
    match cmd[0]:
        # If its a command (not result)
        case '$':
            # if changing directories
            if cmd[1] == 'cd':
                match cmd[-1]:
                    # if going up a directory, remove last entry from cwd list
                    case '..':
                        cwd.pop()
                    # if changing to root dir, set cwd to just root
                    case '/':
                        cwd = ['/']
                    # Otherwise, add directory to stack
                    case other:
                        cwd.append(cmd[-1])
        
        # if 'ls' result is a directory, create dictionary entry for it
        # key will be ALL of the items in the cwd stack + the new ls result
        case 'dir':
            dirs["".join(cwd) + cmd[-1]] = 0
        # Otherwise, the result is a file. Add its size to the dictionary result
        case other:
            dirs["".join(cwd)] += int(cmd[0])
            # Update the dicrectories that are in the current path to have the size of the newest file
            # i.e. update the parent direcroty sizes
            for i in range(1, len(cwd)):
                dirs["".join(cwd[:-i])] += int(cmd[0])

# Find the sum of directories which are smaller than or equal to 100,00
part_1 = sum(
    value for value in dirs.values() if value <= 10**5
)
print(f"Part 1: {part_1}")

# Find the minimum value of a directory size that can be deleted to satisfy the  disk requirements
part_2 = min(
    [value for value in dirs.values() if value >= dirs['/'] - disk_size + needed_size]
)

print(f'Part 2: {part_2}')