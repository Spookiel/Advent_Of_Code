
import re
from collections import defaultdict, Counter
from itertools import permutations, combinations,product
from functools import lru_cache
adj4 = [[0,1], [1,0], [-1,0], [0,-1]]
adj8 = adj4+[[1,1], [-1,-1], [1,-1], [-1,1]]

def lmii(delim=" "):
    return list(map(int, input().split(delim)))

data = """1007125
13,x,x,41,x,x,x,x,x,x,x,x,x,569,x,29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,23,x,x,x,x,x,x,x,937,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,17"""


test1 = """939
7,13,x,x,59,x,31,19"""
test2 = """"""
test3 = """"""
test4 = """"""





def solve(data):

    lines = [i for i in data.splitlines()]

    targ = int(lines[0])
    bs = [i for i in lines[1].split(",") if i!="x"]

    for timestamp in range(targ, targ+50):

        for bus in bs:
            if timestamp%int(bus)==0:
                print(bus, timestamp)
                input()
                break



#solve(test1)
#solve(test2)
#solve(test3)
#solve(test4)

solve(data)






