from functools import lru_cache
import re
from collections import defaultdict, Counter
from itertools import permutations, combinations,product
from functools import lru_cache
adj4 = [[0,1], [1,0], [-1,0], [0,-1]]
adj8 = adj4+[[1,1], [-1,-1], [1,-1], [-1,1]]

def lmii(delim=" "):
    return list(map(int, input().split(delim)))

data = """77
10
143
46
79
97
54
116
60
91
80
132
20
154
53
14
103
31
65
110
43
38
47
120
112
87
24
95
33
104
73
22
66
137
21
109
118
63
55
124
146
148
84
86
147
125
23
85
117
71
48
136
151
130
83
56
140
9
49
113
131
133
74
37
127
34
32
106
1
78
11
72
40
96
17
64
92
102
123
126
90
105
57
99
27
70
98
111
30
50
67
2
155
5
119
8
39"""


test1 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
test2 = """"""
test3 = """"""
test4 = """"""





def solve(data):


    nums = [int(i) for i in data.splitlines()]
    nums.append(max(nums)+3)
    d = [0 for i in range(5)]
    cur = [0]
    numscop = nums[:]
    while cur:
        ne = cur.pop(0)
        try:
            nething = min([j for j in nums if j <= ne+3])
            cur.append(nething)
            nums.remove(nething)
            d[nething-ne] += 1
        except:
            break

    print(d[1]*d[3])


    nums = sorted(numscop)

    @lru_cache(maxsize=None)
    def solve(used, large):
        if used < 0:
            return 0
        if large == max(nums):
            return 1


        total = 0
        for nething in range(1,4):
            if nething+large in nums:
                total += solve(used-1, nething+large)
        return total
    print(solve(len(nums), 0))



solve(test1)
#solve(test2)
#solve(test3)
#solve(test4)

solve(data)






