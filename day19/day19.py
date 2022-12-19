import numpy as np

from collections import deque, defaultdict, Counter
from time import perf_counter
from itertools import chain, cycle
from functools import cache
from copy import copy, deepcopy
from multiprocessing import Process, Queue

def helper(gBest, blueprint: dict, robots: dict,
          resources: dict, mins=24) ->int:

    if mins == 0:
        return resources['geode']
    #if resources['geode'] + ... < gBest[0]:
    #    return gBest[0]

    # Geode bot
    if blueprint['rb_geode']['ore'] <= resources['ore'] and blueprint['rb_geode']['obsidian'] <= resources['obsidian']:
        lBots = robots.copy()
        lRsc = resources.copy()

        lRsc['ore'] -= blueprint['rb_geode']['ore']
        lRsc['obsidian'] -= blueprint['rb_geode']['obsidian']
        # get more resources
        for key in lRsc:
            lRsc[key] += lBots[key]

        lBots['geode'] += 1

        gBest[0] = max(gBest[0],
            helper(gBest, blueprint, lBots, lRsc, mins-1)
        )
    
    # OBSIDIAN BOT
    if blueprint['rb_obsidian']['ore'] <= resources['ore'] and blueprint['rb_obsidian']['clay'] <= resources['clay']:
        lBots = robots.copy()
        lRsc = resources.copy()
        
        
        lRsc['ore'] -= blueprint['rb_obsidian']['ore']
        lRsc['clay'] -= blueprint['rb_obsidian']['clay']
        # get more resources
        for key in lRsc:
            lRsc[key] += lBots[key]
        lBots['obsidian'] += 1

        gBest[0] = max(gBest[0],
             helper(gBest, blueprint, lBots, lRsc, mins-1)
        )

    # CLAY BOT
    if blueprint['rb_clay']['ore'] <= resources['ore']:
        lBots = robots.copy()
        lRsc = resources.copy()

        
        lRsc['ore'] -= blueprint['rb_clay']['ore'] # remove the ore used to make robot
        # get more resources
        for key in lRsc:
            lRsc[key] += lBots[key]

        lBots['clay'] += 1      # add robot

        gBest[0] = max(gBest[0],
             helper(gBest, blueprint, lBots, lRsc, mins-1)
        )

    # ORE BOT
    if blueprint['rb_ore']['ore'] <= resources['ore']:
        lBots = robots.copy()
        lRsc = resources.copy()

       
        lRsc['ore'] -= blueprint['rb_ore']['ore'] # remove the ore used to make robot
        # get more resources
        for key in lRsc:
            lRsc[key] += lBots[key]
        
        lBots['ore'] += 1      # add robot

        gBest[0] = max(gBest[0],
             helper(gBest, blueprint, lBots, lRsc, mins-1)
        )

    for resource in resources:
        resources[resource] += robots[resource]
    gBest[0] = max(gBest[0],
        helper(blueprint, robots, resources, mins-1)
    )

    return gBest[0]


def backtrace(out_q: Queue, bpNo: int, 
              blueprint: dict, resources:dict, robots: dict,
              mins=24) -> None:
    
    best = 0
    result = helper([best], blueprint, robots, resources, mins)

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
            'rb_ore': {'ore' :int(sp[1].split('costs')[1].split()[0])},
            'rb_clay': {'ore': int(sp[2].split('costs')[1].split()[0])},
            'rb_obsidian': {'ore': int(sp[3].split('costs')[1].split()[0]),
                         'clay': int(sp[3].split('and')[1].split()[0]) 
                        },
            'rb_geode': { 'ore': int(sp[4].split('costs')[1].split()[0]),
                        'obsidian': int(sp[4].split('and')[1].split()[0])
                     }
        }
        blueprints[bprint_no] = things
    
    q = Queue()
    for i, blueprint in enumerate(blueprints):
        print(f'Processing  Blue Print #{i+1}...')
        p = Process(target=backtrace,
            args=(q, blueprint, deepcopy(blueprints[blueprint]),
                deepcopy(resources), deepcopy(robots),
                mins
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