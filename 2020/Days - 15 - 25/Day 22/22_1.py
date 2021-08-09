
import re
from collections import defaultdict, Counter
from itertools import permutations, combinations,product
from functools import lru_cache
adj4 = [[0,1], [1,0], [-1,0], [0,-1]]
adj8 = adj4+[[1,1], [-1,-1], [1,-1], [-1,1]]

def lmii(delim=" "):
    return list(map(int, input().split(delim)))

data = """Player 1:
26
8
2
17
19
29
41
7
25
33
50
16
36
37
32
4
46
12
21
48
11
6
13
23
9

Player 2:
27
47
15
45
10
14
3
44
31
39
42
5
49
24
22
20
30
1
35
38
18
43
28
40
34"""


test1 = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""
test2 = """"""
test3 = """"""
test4 = """"""





def solve(data):
    p1,p2 = data.split("\n\n")

    p1 = [int(i) for i in p1.splitlines()[1:]]
    p2 = [int(i) for i in p2.splitlines()[1:]]

    while p1 and p2:
        a,b = p1.pop(0), p2.pop(0)
        if a > b:
            p1.append(a)
            p1.append(b)
        else:
            p2.append(b)
            p2.append(a)


    tot = 0
    print(p1)
    if p1:
        for i in range(len(p1)):
            tot += (len(p1)-i)*p1[i]
    else:
        for i in range(len(p2)):
            tot += (len(p2)-i)*p2[i]
    print(tot)

solve(test1)
#solve(test2)
#solve(test3)
#solve(test4)

solve(data)






