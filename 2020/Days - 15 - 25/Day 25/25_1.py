
import re
from collections import defaultdict, Counter
from itertools import permutations, combinations,product
from functools import lru_cache
adj4 = [[0,1], [1,0], [-1,0], [0,-1]]
adj8 = adj4+[[1,1], [-1,-1], [1,-1], [-1,1]]

def lmii(delim=" "):
    return list(map(int, input().split(delim)))


def gan(s):
    return list(map(int, re.findall(r"-?\d+", s)))

data = """11239946
10464955"""


test1 = """5764801
17807724"""
test2 = """"""
test3 = """"""
test4 = """"""



def loop(val,snum):
    return (val*snum) % 20201227

def solve(data):


    lines = [gan(i)[0] for i in data.splitlines()]
    start = 1
    snum = 7

    for i in range(1000000000):
        start = loop(start, snum)
        #print(start, i)
        if start in lines:
            g = lines.index(start)
            g = 1-g

            s = 1
            for j in range(i+1):
                s = loop(s, lines[g])
            print(s, "FOUND STEP SIZE", i)
            break








solve(test1)
#solve(test2)
#solve(test3)
#solve(test4)

solve(data)






