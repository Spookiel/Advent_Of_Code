
import re
from collections import defaultdict, Counter
from itertools import permutations, combinations,product
from functools import lru_cache
adj4 = [[0,1], [1,0], [-1,0], [0,-1]]
adj8 = adj4+[[1,1], [-1,-1], [1,-1], [-1,1]]

def lmii(delim=" "):
    return list(map(int, input().split(delim)))

data = """0,14,1,3,7,9"""


test1 = """0,3,6"""
test2 = """"""
test3 = """"""
test4 = """"""

from collections import deque



def solve(data):
    target = 30000000
    nums = list(map(int, data.split(",")))


    last = defaultdict(deque)

    for i in range(len(nums)-1):
        last[nums[i]].append(i+1)
    turn = len(nums)
    while turn < target:

        c = nums[turn-1]
        #print(last[c])
        if len(last[c]) <= 1:
            nums.append(0)
            last[c].append(turn)
            last[0].append(turn + 1)
            if len(last[0]) > 2:
                last[0].pop(0)

            turn += 1
        else:
            new = last[c][-1]-last[c].pop()
            nums.append(new)
            last[new].append(turn+1)
            if len(last[new]) > 2:
                last[new].pop(0)
            turn += 1
    print(nums[-1])



import time

start = time.time()

solve(test1)
#solve(test2)
#solve(test3)
#solve(test4)

solve(data)
print(f"FINISHED {time.time()-start}")
#FINISHED 69.196747...


