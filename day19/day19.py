import numpy as np

from collections import deque, defaultdict, Counter
from time import perf_counter
from itertools import chain, cycle
from functools import cache
from copy import copy, deepcopy
from multiprocessing import Process, Queue

def helper(blueprint: dict, robots: dict, mins=24) ->int:
    # switching from backtrace to BFS
    best = 0
    state = (
        0,  # ore
        0,  # clay
        0,  # obsidian
        0,  # geodes
        robots['ore'],
        robots['clay'],
        robots['obsidian'],
        robots['geode'],
        mins # remaining Mins
    )
    visited = set()
    q = deque([state])
    while q:
        state = q.popleft()
        ore, clay, obsidian, geode, rOre, rClay, rObsidian, rGeode, remianing_mins = state
        best = max(best, geode)

        if remianing_mins == 0:
            continue
        ORE_MAX = max([value['ore'] for value in blueprint.values()])

        if rOre >= ORE_MAX:
            rOre = ORE_MAX
        if rClay >= blueprint['obsidian']['clay']:
            rClay = blueprint['obsidian']['clay']
        if rObsidian >= blueprint['geode']['obsidian']:
            rObsidian = blueprint['geode']['obsidian']

        if ore >= mins*ORE_MAX - rOre*(mins - 1):
            ore = mins*ORE_MAX - rOre*(mins - 1)
        if clay >= mins * blueprint['obsidian']['clay'] - rClay*(mins -1):
            clay = mins * blueprint['obsidian']['clay'] - rClay*(mins -1)
        if obsidian >= mins * blueprint['geode']['obsidian'] - rObsidian*(mins - 1):
            obsidian = mins * blueprint['geode']['obsidian'] - rObsidian*(mins - 1)

        state = (ore, clay, obsidian, geode, rOre, rClay, rObsidian, rGeode, mins)

        if state in visited:
            continue
        else:
            visited.add(state)
        
        assert ore >= 0 and clay >= 0 and obsidian >= 0 and geode >= 0, state
        q.append(
            (
                ore + rOre,
                clay + rClay,
                obsidian + rObsidian,
                geode + rGeode,
                rOre,
                rClay,
                rObsidian,
                rGeode,
                mins - 1
            )
        )
        # use ore to buy an Ore bot
        if ore >= blueprint['ore']['ore']:
            q.append(
                (
                    ore - blueprint['ore']['ore'] + rOre,
                    clay + rClay,
                    obsidian + rObsidian,
                    geode + rGeode,
                    rOre+1,
                    rClay,
                    rObsidian,
                    rGeode,
                    mins - 1
                )
            )
        if ore >= blueprint['clay']['ore']:
            q.append(
                (
                    ore - blueprint['clay']['ore'] + rOre,
                    clay + rClay,
                    obsidian + rObsidian,
                    geode + rGeode,
                    rOre,
                    rClay+1,
                    rObsidian,
                    rGeode,
                    mins - 1
                )
            )
        if ore >= blueprint['obsidian']['ore'] and clay >= blueprint['obsidian']['clay']:
            q.append(
                (
                    ore - blueprint['obsidian']['ore'] + rOre,
                    clay - blueprint['obsidian']['clay'] + rClay,
                    obsidian + rObsidian,
                    geode + rGeode,
                    rOre,
                    rClay,
                    rObsidian+1,
                    rGeode,
                    mins - 1
                )
            )
        if ore >= blueprint['geode']['ore'] and obsidian >= blueprint['geode']['obsidian']:
            q.append(
                (
                    ore - blueprint['obsidian']['ore'] + rOre,
                    clay + rClay,
                    obsidian - blueprint['geode']['obsidian'] + rObsidian,
                    geode + rGeode,
                    rOre,
                    rClay,
                    rObsidian,
                    rGeode+1,
                    mins - 1
                )
            )

    return best

def backtrace(out_q: Queue, bpNo: int, 
              blueprint: dict, robots: dict,
              mins=24) -> None:
    
    best = 0
    # helper(blueprint: dict, robots: dict, mins=24)
    result = helper(blueprint, robots, mins)

    out_q.put(bpNo * result)

def main() -> None:
    data = open('input.txt').read().split('\n\n')
    mins = 24
    resources = defaultdict(int)
    blueprints = defaultdict(dict)
    
    robots = {
        'ore': 1,
        'clay': 0,
        'obsidian': 0,
        'geode': 0
    }

    for line in data:
        sp = line.split('\n')
        bprint_no = int(sp[0].split(' ')[-1].replace(':', ''))
        
        things = {
            'ore': {'ore' :int(sp[1].split('costs')[1].split()[0])},
            'clay': {'ore': int(sp[2].split('costs')[1].split()[0])},
            'obsidian': {'ore': int(sp[3].split('costs')[1].split()[0]),
                         'clay': int(sp[3].split('and')[1].split()[0]) 
                        },
            'geode': { 'ore': int(sp[4].split('costs')[1].split()[0]),
                        'obsidian': int(sp[4].split('and')[1].split()[0])
                     }
        }
        blueprints[bprint_no] = things
    
    q = Queue()
    for i, blueprint in enumerate(blueprints):
        print(f'Processing  Blue Print #{i+1}...')
        p = Process(target=backtrace,
            args=(q, blueprint, deepcopy(blueprints[blueprint]),
                  deepcopy(robots), mins
            )
        )
        p.start()
    
    geodes = []
    # get the values from processes
    for _ in blueprints:
        geodes.append(q.get())
    
    print(f'Geodes: {sum(geodes)}')

if __name__ == '__main__':
    start = perf_counter()
    
    main()
    
    print(f'\nTime: {round((perf_counter() - start) * 1000, 2)} ms')