
import re
from collections import defaultdict, Counter
from itertools import permutations, combinations,product
from functools import lru_cache
from copy import deepcopy
adj4 = [[0,1], [1,0], [-1,0], [0,-1]]
adj8 = adj4+[[1,1], [-1,-1], [1,-1], [-1,1]]

def lmii(delim=" "):
    return list(map(int, input().split(delim)))

data = """#...#...
#..#...#
..###..#
.#..##..
####...#
######..
...#..#.
##.#.#.#"""


test1 = """.#.
..#
###"""
test2 = """"""
test3 = """"""
test4 = """"""





def solve(data):

    grid = defaultdict(int)
    lines = [i for i in data.splitlines()]

    for i in range(len(lines)):
        for j in range(len(lines)):
            if lines[i][j] =="#":
                grid[(j,i,0,0)] = 1
            else:
                grid[(j,i,0,0)] = 0

    print(grid)
    for step in range(6):
        gcop = defaultdict(int)

        for x,y,z,w in list(grid.keys()):
            if 1:
                for nx,ny,nz,nw in product([0,1,-1], repeat=4):
                    dx,dy,dz,dw = nx+x, ny+y, nz+z,nw+w
                    if dx==x and dy==y and dz==z and nw==0:continue
                    if grid[(dx,dy,dz,dw)]==0:
                        grid[(dx, dy, dz,dw)] = 0
                    else:
                        grid[(dx,dy,dz,dw)] = 1

        c = 0
        for cx,cy,cz,cw in list(grid.keys()):
            #print(cx,cy,cz, "CHECKING")
            found = []
            for dx,dy,dz,dw in product([0,1,-1], repeat=4):
                if dx==0 and dy==0 and dz==0 and dw==0: continue
                nx,ny,nz,nw = cx+dx, dy+cy, dz+cz,cw+dw
                if gcop[(nx, ny, nz,nw)]==0:
                    gcop[(nx, ny, nz,nw)] = 0

                #gcop[(nx, ny, nz)] = 0
                found.append(grid[(nx, ny,nz,nw)])
            #print(found, (cx, cy, cz), grid[(cx,cy,cz)], found.count(1))
            if grid[(cx,cy,cz,cw)]==1:
                if found.count(1) in [2,3]:
                    gcop[(cx,cy,cz,cw)] = 1
                    #print(f"ASSIGNING {cx, cy, cz}, {gcop[(cx,cy,cz)]}")
                    c += 1
                else:
                    gcop[(cx,cy,cz,cw)] = 0
            else:
                if found.count(1) == 3:
                    gcop[(cx,cy,cz,cw)] = 1
                    #print(f"ASSIGNING {cx,cy,cz},{gcop[(cx,cy,cz)]}")
                    c += 1

                else:
                    gcop[(cx,cy,cz,cw)] = 0
        print(sum(gcop.values()), c, step)
        grid = deepcopy(gcop)
        #input()
#solve(test1)
#solve(test2)
#solve(test3)
#solve(test4)

solve(data)






