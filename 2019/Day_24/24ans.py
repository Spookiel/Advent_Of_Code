import sys
from collections import defaultdict

G = []
for line in open("inp.txt").readlines():
    G.append([x for x in line.strip()])

DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]
L = 100

R = len(G)
C = len(G[0])
E = defaultdict(list)
V = {}
for r in range(R):
    for c in range(C):
        if r == 2 and c == 2:
            continue
        for level in range(-L, L + 1):
            V[(r, c, level)] = False
            if level == 0 and G[r][c] == '#':
                V[(r, c, level)] = True
            for d in range(4):
                rr, cc = r + DR[d], c + DC[d]
                if 0 <= rr < R and 0 <= cc < C and (rr, cc) != (2, 2):
                    E[(r, c, level)].append((rr, cc, level))
            if r == 0 and level - 1 >= -L:
                E[(r, c, level)].append((1, 2, level - 1))
            if c == 0 and level - 1 >= -L:
                E[(r, c, level)].append((2, 1, level - 1))
            if c == C - 1 and level - 1 >= -L:
                E[(r, c, level)].append((2, 3, level - 1))
            if r == R - 1 and level - 1 >= -L:
                E[(r, c, level)].append((3, 2, level - 1))
            if r == 1 and c == 2 and level + 1 <= L:
                for cc in range(5):
                    E[(r, c, level)].append((0, cc, level + 1))
            if r == 2 and c == 1 and level + 1 <= L:
                for rr in range(5):
                    E[(r, c, level)].append((rr, 0, level + 1))
            if r == 2 and c == 3 and level + 1 <= L:
                for rr in range(5):
                    E[(r, c, level)].append((rr, C - 1, level + 1))
            if r == 3 and c == 2 and level + 1 <= L:
                for cc in range(5):
                    E[(r, c, level)].append((R - 1, cc, level + 1))


def f(V):
    V2 = {}
    for k, v in V.items():
        alive = 0
        for y in E[k]:
            if V[y]:
                alive += 1
        if (V[k] and alive != 1) or (not V[k] and alive not in [1, 2]):
            V2[k] = False
        else:
            V2[k] = True
    return V2


for _ in range(200):
    V = f(V)

ans = 0
for k, v in V.items():
    if v:
        ans += 1
print(ans)
