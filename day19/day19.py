import numpy as np

from collections import deque, defaultdict, Counter
from time import perf_counter
from itertools import chain, cycle
from functools import cache
from copy import copy, deepcopy
from multiprocessing import Process, Queue


def backtrace(out_q: Queue, bpNo: int, blueprint: dict, st_rsc: dict, mins=24) -> None:
    result = 0

    out_q.put(bpNo *result)

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
            'obsidian': {'ore': int(sp[3].split('costs')[1].split()[0]),
                         'clay': int(sp[3].split('and')[1].split()[0]) 
                        },
            'geode': { 'ore': int(sp[4].split('costs')[1].split()[0]),
                        'obsidian': int(sp[4].split('and')[1].split()[0])
                     }
        }
        blueprints[bprint_no] = things
    
    q = Queue()
    for blueprint in blueprints:
        p = Process(target=backtrace,
            args=(q, blueprint, deepcopy(blueprints[blueprint]),
                deepcopy(resources)
            )
        )
        p.start()
    
    geodes = 0
    # get the values from processes
    for _ in blueprints:
        geodes += q.get()
    
    print(f'Geodes: {geodes}')

if __name__ == '__main__':
    start = perf_counter()
    main()
    print(f'\nTime: {round((perf_counter() - start) * 1000, 2)} ms')