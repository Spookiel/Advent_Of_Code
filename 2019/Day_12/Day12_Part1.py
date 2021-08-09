from collections import defaultdict, Counter, deque
import re



data = """<x=5, y=13, z=-3>
<x=18, y=-7, z=13>
<x=16, y=3, z=4>
<x=0, y=8, z=8>"""
test = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""
from itertools import combinations


def score(lines, vels):
    total = 0
    for moon in lines:
        total += sum(map(abs, moon))*sum(map(abs, vels[tuple(moon)]))
    return total


from copy import deepcopy
def step(lines, vels):
    pairs = [i for i in combinations(lines, 2)]
    for first, second in pairs:
        for axis in range(3):
            if first[axis] != second[axis]:
                if second[axis] > first[axis]:
                    vels[tuple(second)][axis] += 1
                    vels[tuple(first)][axis] -= 1
                else:
                    vels[tuple(second)][axis] -= 1
                    vels[tuple(first)][axis] += 1
    new = {}
    for k,v in vels.items():
        ind = lines.index(list(k))
        item = deepcopy(lines[ind])
        for i in range(3):
             lines[ind][i] += v[i]*-1
        lines[ind] = lines[ind]
        new[tuple(lines[ind])] = vels[tuple(item)]
    return lines, new
def solve(data, steps):
    lines = [list(map(int, re.findall(r"-?\d+", i))) for i in data.splitlines()]
    vels = defaultdict(lambda: [0,0,0])
    seen = set()
    for s in range(steps):
        lines, vels = step(lines, vels)
        to_check_vels = tuple(vels.items())
        print(lines, vels)
    print(score(lines, vels))


solve(test, 10)