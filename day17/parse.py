from itertools import cycle

rocks = [
    (0,1,2,3),
    (1,0+1j,2+1j,1+2j),
    (0,1,2,2+1j, 2+2j),
    (0, 0+1j, 0+2j, 0+3j),
    (0, 1, 0+1j, 1+1j)
]
l_rock = len(rocks)
rocks = cycle(rocks)
stack = set()
stored = dict()
top = 0 
rock_idx, jet_idx = 0, 0

# convert jets into -1, and 1 via ord
jets = [ord(ch) - 61 for ch in open('input.txt').read().replace('\n', '')]
l_jets = len(jets)
jets = cycle(jets)
is_empty = lambda pos: pos.real in range(7) and pos.imag > 0 and pos not in stack
check = lambda pos, dir, rock: all(is_empty(pos+dir+r) for r in rock)

for stopped in range(int(1e12)):
    pos = complex(2, top+4)     # from text
    key = rock_idx, jet_idx     # key is a (rock_idx, jet_idx) so limited first arg to 0-4

    if stopped == 2022:
        print(f'2022: {top}')
    
    if key in stored:
        S, T = stored[key]
        # (1E12 - current stopped) // stopped - previously stopped
        d, m = divmod(1e12 - stopped, stopped - S)
        # if they are evenly divisible, then this is a cycle.
        # answer is the current top * (cycle length * cycles)
        if m == 0:
            print(f'TOP : {int(top + (top - T) * d)}')
            break
    else:
        stored[key] = stopped, top
    
    rock = next(rocks)
    rock_idx = (rock_idx+1) % l_rock # just index rotating from 0-4 with wrapping

    while True:
        jet = next(jets)
        jet_idx = (jet_idx+1) % l_jets # same thing here just wayyyyy longer

        # using lambdas is way faster than functions
        if check(pos, jet, rock):
            pos += jet
        if check(pos, -1j, rock):
            pos += -1j
        else:
            break
    
    # could use a for loop but OR is much quicker since it bulk adds things
    stack |= {pos+r for r in rock}
    # checks the current max with the current piece position, PLUS the additional height of piece based on rock_idx 
    top = max(top, pos.imag+[1,0,2,2,3][rock_idx])