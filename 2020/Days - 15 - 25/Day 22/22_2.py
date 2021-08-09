
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



from functools import lru_cache


def play(d1, d2):
    seen = set()

    while d1 and d2:
        if (a := (tuple(d1), tuple(d2))) in seen:
            return d1+d2, []
        else:
            seen.add(a)
        a,b = d1.popleft(), d2.popleft()
        if a <= len(d1) and b <= len(d2):
            r1,r2 = play(deque(list(d1)[:a]), deque(list(d2)[:b]))
            if r1:
                d1.append(a)
                d1.append(b)
            else:
                d2.append(b)
                d2.append(a)
        else:

            if a > b:
                d1.append(a)
                d1.append(b)
            else:
                d2.append(b)
                d2.append(a)
    return d1, d2




from collections import deque



def solve(data):
    p1,p2 = data.split("\n\n")

    p1 = [int(i) for i in p1.splitlines()[1:]]
    p2 = [int(i) for i in p2.splitlines()[1:]]

    ans, ans2 = play(deque(p1),deque(p2))
    #print(ans, ans2)
    tot1 = 0
    for i in range(len(ans)):
        tot1 += (len(ans)-i)*ans[i]

    tot2 = 0
    for i in range(len(ans2)):
        tot2 += (len(ans2)-i)*ans2[i]

    print(tot1, tot2)

solve(test1)
#solve(test2)
#solve(test3)
#solve(test4)

solve(data)






