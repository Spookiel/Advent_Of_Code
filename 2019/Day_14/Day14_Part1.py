from computer import Program
# = Program("0", "14.in", [])
#a.run() is next value
from collections import defaultdict, Counter, deque

import re
pattern = r"-?\d+"


data = """14 FTHZP => 8 NXVR
103 ORE => 1 RHWM
3 JQLZ, 13 ZWNK, 4 JLBM => 4 GTNG
2 VZLV, 2 ZWNK, 3 WNVTN => 5 NWQSK
170 ORE => 4 JZXV
5 PCML, 12 BHVK => 3 PLMZW
2 QCHGV => 9 PCHB
2 NBVQN => 7 NMWJT
1 VXVP, 1 TRPXQ => 9 WQHG
7 JLBM, 26 NMWJT => 8 WVHS
32 TBPB, 1 BHVK => 9 LCQZ
1 KNBSR => 4 PWTQ
155 ORE => 1 VXVP
4 LCQZ => 7 DGTV
143 ORE => 4 FMWHV
1 QBFR, 1 QCHGV, 9 LCMK => 5 GRTNC
20 NXVR, 2 PLMZW => 3 LHPC
1 GTNG, 33 VZLV, 5 LHPC, 4 WVHS, 2 PLMZW, 1 GRTNC, 1 LCQZ => 2 BMKLF
1 SQRH, 3 RJSR, 2 DZTDK, 14 WVHS, 9 PCHB, 9 NWQSK, 1 PCML => 7 RSXWV
1 LCMK, 5 WVHS, 1 DZVH => 1 JQLZ
117 ORE => 6 VDND
3 VDND => 1 FTHZP
1 PWTQ, 1 VZWZ, 13 NBVQN => 9 PCML
1 RHWM => 1 FRLXT
5 WBHBG, 1 JZXV => 3 QCHGV
6 JZXV => 7 WBHBG
14 FMWHV => 2 TRPXQ
22 FTHZP, 4 XMCX => 8 ZWNK
8 LCXZ => 9 QBFR
21 QCHGV => 6 QTQDQ
4 GTNG => 4 DZTDK
1 VDND, 2 VXVP => 8 KNBSR
8 XMBW => 8 NBVQN
3 SPQKS => 2 LTSHN
3 VZWZ => 6 XSXB
1 XSXB => 5 WNVTN
1 LHPH, 33 DZVH, 8 PCHB => 9 VZWZ
5 XMBW, 1 WVHS => 9 QPXNT
1 GBJFW, 3 XHFZ, 22 JLBM => 3 LCXZ
17 KNBSR => 7 XMBW
8 WVHS => 8 VZLV
2 NMWJT, 7 NXVR, 6 LNVPT => 9 TWVWC
1 SQRH => 9 RJSR
8 JLBM, 15 GBJFW => 5 TBPB
15 DGTV => 7 TVXN
11 KJPQ, 10 VDND => 6 SQRH
2 TRPXQ => 2 DZVH
10 WBHBG, 1 KJPQ => 5 JLBM
12 PCHB => 9 BHVK
5 WQHG => 5 SPQKS
7 PWTQ, 13 TRPXQ => 4 MKFD
2 NBVQN, 2 TBPB, 6 BHVK => 5 LNVPT
3 MKFD, 15 KNBSR, 2 WBHBG => 3 KJPQ
3 MKFD => 6 LCMK
1 PWTQ, 1 QTQDQ, 4 LNVPT => 9 WVXD
2 PCHB, 14 KNBSR, 5 LTSHN => 1 GBJFW
1 DGTV, 1 TVXN, 21 LHPC, 4 GBJFW, 11 TWVWC, 1 WQHG, 18 LCXZ => 4 KJNJ
96 RHWM, 6 KJNJ, 1 BMKLF, 20 TVXN, 16 RSXWV, 3 RJSR, 53 QPXNT, 26 WVXD => 1 FUEL
1 FRLXT => 4 LHPH
2 XHFZ => 6 XMCX
2 XMBW, 22 FTHZP => 9 XHFZ"""
test = """171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX"""

import math
def solve(data):
    lines = [i.split("=>") for i in data.splitlines()]
    d = {}
    queue = []
    need = defaultdict(int)
    for line in lines:
        before, after = line[0].strip().split(", "), line[1].strip().split(", ")
        to_put = []
        for bef in before:
            to_put.append(tuple(bef.split()))
        d[tuple(after[0].split())] = to_put
    for k in d.keys():
        if "FUEL" in k:
            for v in d[k]:
                queue.append(v)
                need[v[1]] = int(v[0])
    print(need)
    print(queue)
    total = 0
    while queue or len(need) > 1:
        val, name = queue.pop(-1)
        val = int(val)

        for k in d.keys():
            if name in k:

                to_make = math.ceil(need[k[1]] / int(k[0]))
                print(to_make, need, "here")
                if len(d[k])==1 and d[k][0][1]=="ORE":
                    total += to_make*int(d[k][0][0])
                    del need[k[1]]
                else:

                    for v in d[k]:
                        need[v[1]] += int(v[0])*to_make
                        queue.append(v)
                    del need[k[1]]



test = """2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF"""


#solve(test)
from copy import deepcopy

def p1(s):
    n,item = s.split()
    return int(n),item

OIN = {}
F = {}
for line in open('14.in').readlines():
    line = line.strip()
    need,get = line.split(' => ')
    nget,get = p1(get)
    need = need.split(', ')
    need = [p1(s.strip()) for s in need]
    for (n,y) in need:
        if y not in OIN:
            OIN[y] = 0
        OIN[y] += 1
    #print(line,nget,get,need)
    assert get not in F
    F[get] = (nget,need)


print(OIN)
def cost(nfuel):
    IN = deepcopy(OIN)
    IN['FUEL'] = 0
    REQ = {'FUEL': nfuel}
    done = False
    while not done:
        for x in IN:
            if IN[x] == 0:
                n = REQ[x]
                #print(x,n)
                if x == 'ORE':
                    return n
                (nget,need) = F[x]
                amt = (n+nget-1)//nget
                for (ny,y) in need:
                    if y not in REQ:
                        REQ[y] = 0
                    REQ[y] += amt*ny
                    IN[y] -= 1
                del IN[x]
                break
"""
low = 0
high = int(1e12)
while low < high:
    mid = (high+low+1)//2
    if cost(mid) < int(1e12):
        low = mid
    else:
        high = mid-1
print(low)"""