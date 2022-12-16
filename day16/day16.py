from collections import defaultdict
from functools import cache
from time import perf_counter

with open('input.txt', 'r') as fh:
    data = fh.readlines()

valves = defaultdict(tuple)

for line in data:
    sp = line.split()
    name = sp[1].strip()
    flow = int(sp[4][5:-1]) # after eq sign to last integer char
    conns = [a.replace(',', '') for a in sp[9:]]
    
    valves[name] = (flow, conns)

part_1 = True
@cache
def search(current: str, opened: frozenset,  mins=30) ->int:
    if mins > 0:
        pressure = 0
        flow, conns = valves[current] # tuple of flow(int) and conns(list)

        # loop over the connections to current node
        # find the maximum pressure in a given path FROM THE CURRENT VALVE
        for valve in conns:
            pressure = max(
                pressure, 
                search(valve, opened, mins - 1)
            )
        
        # if the current one isn't open, open it if rate > 0 
        if flow > 0 and current not in opened:
            opened = set(opened)        # convert from frozenset to set 
            opened.add(current)         # Add the cuurent valve 

            mins -= 1                   # Decrement mins
            new_pressure = mins * flow  # Get pressure from this valve
            for valve in conns:
                pressure = max(
                    pressure, 
                    # have to pass the frozenset of this set so that its potentially unique to each valve.
                    # i.e. cause we can potentially open more valves in X path but not Y
                    new_pressure + search(valve, frozenset(opened), mins - 1)
                )
        return pressure
    else:
        return 0

@cache
def search_2(current: str, opened: frozenset,  mins=30) ->int:
    if mins > 0:
        pressure = 0
        flow, conns = valves[current] # tuple of flow(int) and conns(list)

        # loop over the connections to current node
        # find the maximum pressure in a given path FROM THE CURRENT VALVE
        for valve in conns:
            pressure = max(
                pressure, 
                search_2(valve, opened, mins - 1)
            )
        
        # if the current one isn't open, open it if rate > 0 
        if flow > 0 and current not in opened and mins > 0:
            opened = set(opened)        # convert from frozenset to set 
            opened.add(current)         # Add the cuurent valve 

            mins -= 1                   # Decrement mins
            new_pressure = mins * flow  # Get pressure from this valve
            for valve in conns:
                pressure = max(
                    pressure, 
                    # have to pass the frozenset of this set so that its potentially unique to each valve.
                    # i.e. cause we can potentially open more valves in X path but not Y
                    new_pressure + search_2(valve, frozenset(opened), mins - 1)
                )
        return pressure
    else:
        return search('AA', frozenset(), mins=26)


print('Starting Part 1...')
start = perf_counter()
part_1_answer = search('AA', frozenset())
print(part_1_answer)
stop = perf_counter()
print('Part 1 ran in: {} ms'.format(round((stop-start) * 1000, 2)))

# part 2 is searching from t = 1 to 26 twice
# IF THE MINS for the 2nd pass is 0, then need to run the search again for 'elephant'
part_2 = False
start2 = perf_counter()
ans2 = search_2('AA', frozenset(), 26)
print(ans2)
stop2 = perf_counter()
print('Part 2 ran in: {} ms'.format(round((stop2-start2) * 1000, 2)))

speed_up = (stop - start) / (stop2 - start2)
print(f'Cache sped up part 2 by a factor of: {round(speed_up,2)}')
