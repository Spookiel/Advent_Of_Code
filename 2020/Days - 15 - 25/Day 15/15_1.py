
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





def solve(data):
    target = 30000000
    nums = list(map(int, data.split(",")))


    last = defaultdict(list)

    for i in range(len(nums)-1):
        last[nums[i]].append(i+1)
    turn = len(nums)
    while turn < target:
        #print(nums, last, nums[turn-1])
        #input()
        c = nums[turn-1]
        if len(last[c]) <= 1:
            nums.append(0)
            last[c].append(turn)
            last[0].append(turn+1)
            turn += 1
        else:
            new = last[c][-1]-last[c][-2]
            nums.append(new)
            last[new].append(turn+1)
            last[new] = last[new][-2:]
            turn += 1
    print(nums[-1])





solve(test1)
#solve(test2)
#solve(test3)
#solve(test4)

solve(data)






