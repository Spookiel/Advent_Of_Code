import re
from collections import defaultdict, deque, Counter

data = """#################################################################################
#.#...........#...#.....#.......#...#...#.....#.....#.....#...#...#..g.........x#
#.#.#####.###Z#.#.#.###.#.#.###.#.###.#.#.###.#.#####.#.#.#.#.#.###.###########.#
#...#...#.#.....#.#.#.#...#.#...#.#...#.#.#.#.#.#.....#p#.#.#.#.......#...#.....#
#.#####.#.#########.#.#####.#.###.#.###.#.#.#.#.#.#####.#.#.#.#######.###.#.###.#
#.......#...#.......#.....#.#.#.....#...#.#.....#...#...#...#.#.....#.....#.#...#
###########.#.#########.###.#.###.###.###.#####.###.#.#######.#.###.#####.#.#.###
#...V.....#.......#...#.#...#...#...#...#.#...#...#.#.#.......#.#.#.#.....#.#...#
#.#######.#######.#.#.#.#.#####.#######.#.#.#.#.###.#.#######.#.#.#.#.#####B###.#
#.#.......#...#.....#...#.....#.....#...#...#.#.#...#.......#...#...#.....#...#.#
#.#.#####.#.#K#.#############.#####.#.#.#####.###.#########.#####.#######.###.###
#.#.#.....#.#.#...#...#.......#...#.#.#.#...#.#...#...#.....#.....#....l..#.#...#
#.#.#####.#.#.###.#.#.#.#######.#.#.#.###.#.#.#.###.#.#.#####.#######.#####.###.#
#.#.....#.#.#...#.#.#.#.....#...#...#...#.#...#.#...#.#...#...#.....#.........#.#
#.#####.#.#.###.#.#.#.#####.#####.#####.#.#####.#.#.#####.#.###.###.#######.###.#
#.#...#.#.#...#.#.#.#..j..#.....#.......#.#...#...#.#...#.#.....#...#.......#...#
#.#.###.#Q###.#.###.#####.#####I#######.#.#.#.#.#####.#.#.#######.#######.###.#.#
#...#...#.#...#.....#...#.....#.....#...#.#.#...#.....#.#.#.#.....#.....#h..#.#.#
###.#.#####.#########.#.#####.#.###.#.###.#.#####.#####.#.#.#.#####.###.#####.#.#
#...#...#...#.......#.#.......#...#.#...#.#.#.....#.....#.#.....#.....#.......#.#
#.#####.#.###.#####.#.###########.#.#####.#.#.#####.#####.#.###.#####.###########
#.....#.#...#.#.....#.#.......#...#.#...#...#.#.......#...#.#.#.....#.....#.....#
#####.#.###.#.#.###.###.###.###.###.#.#.#####.#######.###.###.#####.#####.#.###.#
#.#...#...#.#.#.#...#.....#...#.#.#.#.#.#.....#...#.#.....#...#...#.....#.....#.#
#.#.###.###.###.#.###########.#.#.#.#.#.#.#.###.#.#.#####.#.#####.#####.#######.#
#.#...#...#.....#.#..e....#...#...#...#.#.#.#...#.#...#...#.....#.....#.#.......#
#.###.###.#######.#.#####.#.#####.#####.#.###.###.#.#.#.#######.#.#.###.#.#####.#
#.#...#.#...#...#...#.....#.#.........#.#.#.....#.#.#.#.......#.#.#.....#...#...#
#.#.###.#.###.#.#####.#####.#.#########.#.#.#####.###.###.#####.#.#########.#.###
#...#...#...#.#.....#.#.#.......#...#...#.#o#.#...#...#...#.....#.#.........#...#
#.#####.###.#.#.#####.#.#.#######.#.#.#.#.#.#.#.###.###.###.#####.#####.#######U#
#.........#...#...#...#...#.......#...#.#.....#...#.....#.#.#...#.#.....#.....#.#
#########.#######.#.###.###.###########.#.#######.#.#####.#.#.#.#.#.#########.#.#
#.......#.......#...#.....#...#.#.....#.#.#.....#.#.......#.#.#.#.#.#.......#...#
#.#####.#######.#############.#.#.#.###.#.#.###.#.#########.#.###.#.#.#####.#####
#.....#.#.......#.....#.......#.#.#.#...#.#.#.....#...#.....#.#...#.....#.#..tE.#
#.###.###.#######.###.#.#######.#.#.#.###.#.#######.#.#.#####.#.#######.#.#####.#
#.S.#...#.....#...#.#c..#...#.....#.#.#.#.#...#.....#..s#.....#.#.....#...#...#.#
###.###.#####.#.###.#####.#.#.#####.#.#.#.###.#.#########.###.#.###.#.#####.#.#.#
#.....#.........#.........#.......#.........#...#...........#.....F.#.......#...#
#######################################.@.#######################################
#m........#.............#...........#.........#.....#.........#.....#...#.......#
###.#####.#########.#####.#####.###.#.#.#.#.#.#.###.#.#####.#.#.###.#.#.#.###.#.#
#...#.#...#.......#...#...#...#.#.#...#.#.#.#.#...#...#...#.#.....#.#.#.#.#...#.#
#.###W#.###.#####.#.#.#O###.#.#.#.#####.###.#####.#####.#.#########.#.#.#.#.###.#
#.#.......#...#.#.#.#.#...#.#.#.#...#...#...#...#.....#.#.#...#...#.C.#.#.#.#...#
#.#######.###.#.#.#.#.###.#.#.#.#.###.###.###.#.#.#####.#.#.#.#.#.#####.#.#.###.#
#.#...#.#.#...#...#.#.#...#.#...#.......#.....#...#.....#.#.#.#.#.....#...#...#.#
#.#.#.#.#.#.###.###.#.#.###.#####.#######.#########.#####.#.#.#.#####.#.#####.#.#
#.#f#.#.#.#.#.#.#...#...#...#...#...#...#.#.......#...#.....#.#.#...#.#...#.#.#.#
#.#.#.#.#.#.#.#.#.#######.###.###.###.#D#.###.#.#####.#######.#.#.###.###.#.#.#.#
#...#.#...#.#...#.....#.#...#.....#...#.#...#.#.#...#.....#.#.#.#.....#.....#.#.#
#####.#.###.#.#######.#.###.###.###.###.###.#.###.#.#####.#.#.#.#.#####.#####.#.#
#.....#...#.#.#...#...#...#...#.#a..#.#.#.#.#.....#.....#.#...#.#w#...#...#...#.#
#.#######.#.#.#.#.#.###.#####.###.###.#.#.#.#.#######.###.#.###.#.#.#####.#.###.#
#.#.....#.#.#.#.#.#...#.#...#...#...#.#.#...#.....#...#...#...#.#.#.......#.#...#
#.###.#.#.#.#.#.#.###.#.#.#.#.#.###.#.#.#.#########.#.#.#####.#M#.#########.###.#
#...#.#...#.#...#.#.....#.#.#.#...#.#..d#.#.........#.#.#.......#...#.....#...#.#
#.#.#.#####.#####.#######.#.#####.#.#.###.###.#####.###.#.#########.#.###.###.#.#
#.#.#...#...#.............#.......#.#...#.#i..#.....#...#.#.......#...#.#...#.#.#
###.###.#.###.#################.###A###.#.#.###.#####.###.#.#####.#####.###.#.###
#...#.....#.#.#.....#.Y...#...#.#...#.#.#...#.#.#.#...#...#.#.N...#.........#...#
#.###.#####.#.#.###.#####.###.#.#.###.#.#####.#.#.#.###.###.#############.#####.#
#...#.#...#...#.#.#.....#...#...#.#...R.#.#.....#.#...#...#.....#...#...#q....#.#
#.#.###.#.#.###.#.###.#.###.#####.#.#####.#.#####.###.#########.#.#.#.#.#####.#.#
#.#...#.#.#.#...#...#.#...#..y....#.#...#.#.#.......#.........#...#...#...#.#.#.#
#####.#.#.###.###.#.#.###.#########.#.#.#.#.#.#####.#########.###########.#.#.#.#
#...#.#.#...#.#...#.#...#.....#...#.#.#.#.#.#.#.............#.#...#.....#.#.#.#.#
#.#.#.#.###.#.#.#######.#####.#.#.#.###.#.#.#.#.#######.#####.#.#.#.###.#.#.#.#.#
#.#...#.#.#.#...#.......#...#.#.#r..#...#...#.#.#.....#.#...#...#.#...#...#.#.#.#
#T###.#.#.#.###.#.#######.#.###.#####.###.#####.#.###.#.#.#.#####.###.#####.#.#.#
#.#...#u..#.....#...#...#n#...#.#.#.....#.#...#.#...#.#.#.#.#.......#.....#.....#
#.#.#####.#########.#.#H#.###.#.#.#.###.#.#.#.#.#.###.#.#.#J#.###########.#####.#
#.#.....#.#...#...#.#.#...#.#...#.#...#.#...#.#...#...#.#.#...#.........#.....#.#
#.#######.#.###.#.#.#.#####.#####.###.#.#####.#.###.#####.#.###.#####.#######.#.#
#.#.......#.#...#...#...#.....L.#.....#.#.#...#..v#z..#...#.#...#...#.......#.#.#
#.#.#######.#.###.#####.#.#####.#######.#.#.#########.#.#####.###.#.###.#####.#.#
#.#.#k......#...#.#...#...#.....#.....#.#.#.....#...#.#..b....#...#...#...#...#.#
#.#.#.#####.###.###.#.#####.#####.###.#.#.#####.#.#.#.#############.#.###X#.###.#
#.....#.......#...G.#.............#.....#.........#...P.............#...#...#...#
#################################################################################"""


test = """########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################"""

import networkx as nx
def solve(data):
    pattern = r"-?\d+"
    lines = [[j for j in i] for i in data.splitlines()]
    width = len(lines[0])
    height = len(lines)
    keys = {}


    G = nx.grid_2d_graph(width, height)
    for y in range(height):
        for x in range(width):
            if lines[y][x]=="#" or lines[y][x] in "QWERTYUIOPASDFGHJKLMNBVCXZ":
                G.remove_node((x, y))
            elif lines[y][x] in "abcdefghijklmnopqrstuvwxyz":
                keys[(x, y)] = lines[y][x]
            elif lines[y][x]=="@":
                start = x, y
    total = 0
    found = set()
    for _ in range(10):
        possible = nx.single_source_shortest_path_length(G, start)
        print([i for i in possible.keys() if i in keys.keys()], "here", start)
        for m in possible.keys():
            if m in keys.keys() and m not in found:
                print(m, keys[m], possible[m])
                total += possible[m]
                to_remove = None
                for yd in range(len(lines)):
                    for xd in range(len(lines[0])):
                        if lines[yd][xd]==keys[m].upper():
                            #print(lines[yd][xd], "HERE")
                            to_remove = xd, yd
                #print("FOUND KEY", keys[m], "REMOVING AT", to_remove)
                if to_remove is not None:
                    G.add_node(to_remove)
                    for adj in [[0,1], [0,-1], [1,0], [-1,0]]:
                        newx, newy = to_remove[0]+adj[0], to_remove[1]+adj[1]
                        if 0 <= newx < len(lines[0]) and 0 <= newy < len(lines):
                            if lines[newy][newx] != "#":
                                #print("ADDED EDGE", to_remove, newx, newy)
                                G.add_edge(to_remove, (newx, newy))
                    del keys[m]
                    start = m
                    found.add(m)
                    break

    print(total)
import itertools
def bfs(graph):
    pass
from copy import deepcopy
def solve2(data):
    lines = [[j for j in i] for i in data.splitlines()]
    width = len(lines[0])
    height = len(lines)
    G = defaultdict(list)
    keys = {}
    queue = []
    seen = set()
    doors = {}
    keyConvert = {}
    for y in range(height):
        for x in range(width):
            if lines[y][x]=="@":
                start = x, y
            elif lines[y][x] in "qwertyuiopasdfghjklzxcvbnm":
                print("FOUND KEY", x, y, lines[y][x])
                keys[(x, y)] = lines[y][x]
                keyConvert[lines[y][x]] = (x, y)
            elif lines[y][x] in "QWERTYUIOPASDFGHJKLZXCVBNM":
                doors[(x, y)] = lines[y][x]


    queue.append((start, []))
    while queue:
        pos, comes_after = queue.pop(-1)
        seen.add(pos)
        for adj in [[0,1], [1,0], [-1, 0], [0,-1]]:
            newx, newy = pos[0]+adj[0], pos[1]+adj[1]
            if (newx, newy) not in seen:
                cop = deepcopy(comes_after)
                if lines[newy][newx] in "qwertyuiopasdfghjklzxcvbnm":
                    G[(newx, newy)].extend(cop)
                    cop.append(lines[newy][newx])
                    queue.append(((newx, newy), cop))
                elif lines[newy][newx] != "#":
                    G[(newx, newy)].extend(cop)
                    queue.append(((newx, newy), cop))
    print(keyConvert, "HERE")
    print(G, "GRAPH")
    recurse(G, [], doors, keys, keyConvert)
    order = ['I', 'Z', 'V', 'K', 'Q', 'S', 'O', 'T', 'G', 'L', 'H', 'R', 'D', 'A', 'Y', 'W', 'F', 'E', 'B', 'U', 'C', 'M', 'J', 'X', 'N', 'P']



def recurse(G, unlocked, doors, keys, doorConvert):
    for position in G.keys():
        if len(G[position])==1:
            cop = deepcopy(unlocked)
            cop.append(G[position][0])
            recurse(unlock(doorConvert[G[position][0]], doors, G), cop, doors, keys, doorConvert)
    if unlocked:
        print("FOUND", unlocked, len(unlocked), len(doors.items()))


def find_distance(start, finish, graph):
    queue = []
    seen = set()
    queue.append((start, 0))
    while queue:
        n = queue.pop(0)



def unlock(doorPos, doors, G):
    for i in G.keys():
        try:
            G[i].remove(doors[doorPos])
        except:
            pass
    return G
solve2(test)
