
import re
from collections import defaultdict, Counter
from itertools import permutations, combinations,product
from functools import lru_cache
adj4 = [[0,1], [1,0], [-1,0], [0,-1]]
adj8 = adj4+[[1,1], [-1,-1], [1,-1], [-1,1]]

def lmii(delim=" "):
    return list(map(int, input().split(delim)))

data = """nweneneeneneneneneesweenene
seswswswswnwswnenwswweseswseswswseswsenw
enweneswneneesenenenenenenene
nwseenwsewneseseseswneeenwewseenwnw
wwweseswnwwwswwwwnweswwew
weeneseeneeswswneswseeeeeee
nwseswnwswwnwnwwweneseswenenenwwe
nwnwwswesenwewwnenwsenenwnwnwswnwnwese
sweswseswsenwseswswswswsw
senesenenesewnwswesewneswseesesee
seenewwewwwwswswwwnewsewnwww
wswneswswsewwseswswnwswswnese
seseeeswewseswsweeseenwnenwwnwnwnw
nwnwnenwnenwsewswnwnwsewnwnwnwwwwwnw
wneweswwsenwwwswnwwew
swwswwewsewwwwwwwwwnw
swswewnwseseswnenenewswwswsweswsesese
seswseewnenwnweswnesweenwswnenenenee
nwswnenwneswenwnwnewneneswnwsesenwnee
nwsenenewwsenwsewwewnwwswwseeswsw
swseseeneewseeeeesesenesenwewseee
eneeeeneneewswwnenenenenenenenene
wwneweneesenwneeesweeneweesee
nwneneneneenenwnenwneswneswnwnewwneene
wseneeneewwwsesewenesenewwnenese
weeseneneenesesenenenenwnwswnewnew
swsweswenenwswnenwneneneseseswnwswseswe
swsewwwswsenwnwswww
nwnwnwswnwnwenwnwnwnenwnwsenwnwwwnwnw
senwneseseseeneeseeseeeseseswswenwse
nwsweseneneswwesenesweswneswwwswswwsw
nwnwnwnwnwnwnwnwenwwewnwswnwnwsenwnwnw
seseseeneswswwseswnwnwswseeseswneewww
eswnwseswswsweswesesewseswnesewswswsw
wnwswseneneneseseswwswswsw
eeneneseeweseeweeeneswnenwnenwsesw
seseswsewneseswenewsesesesenwseeewe
nwswnwwwnwewewwnwsw
eenwweeeeeeseenwseseneswsesee
eseeswnenwneneenenesenenwnwnenenenesw
senwsweenweeneneenwseneeesweene
swswswwweswsweswswswswseenenwswwsww
esenwneseseneneswnwnenwneeswesenwwne
eseseeesweeseseewseesewsenwsese
sewewnwnwwswewnwnwnwnwwnwnwnwww
seseewseeeneeeewseese
esenwneswnwewnwneneswneeneneesenene
eswswseenweeswnenesewenwnenwsweswee
ewenweeeneseeewseeseseeneswsew
eswseseseswswsesew
wesenweswwnesewseseeneswswswsenwse
sesewewseseesewnweenesenwseesw
swwneswswseneseseseewseswsesesesenwsenwsw
nwswnwswseswnwwseswswswseswnwseeenese
neeswwswwnwsenwsewseneswseweseneene
swwswsesesesenenwsenenwsweseseswsw
seeesewesesenwneeseese
seseenwseseswsesewseneese
senwseneswsewsesweseseseseseseswseswne
nwsenewnwneneseswneseenwneswneenwwnw
wswwwenwwwwsewnwnwesenwnwnwnenww
nwseswswswswswswswswswwswswsw
newwswwswnesewwwswswwswsweswwswsw
swewwnwnwewseswwswswsewsww
nwseeeseeeseeeesesenwnwsweeeee
senenwseesewswseneweeenwseswseseese
neneneswnenwnenenenwnesenwnesenenesenewe
wnesenwsenwseseswneseeswsesenenw
eswseseseswnenwnwswswseswseswseseseswse
seenwswnenwswnwnwnwswnwnwnwnenwnwnwnwnw
nenwsewewswneswenenwneneeswnwneesesw
nenenewnenwnweneneeswwnenwneneseesene
wwwwswwswnewseeneneswswwswsw
wneneeeneeesweneneenesenewneeee
eneeeeneeeeeeweseenenwseew
eewwsweneenwwseweeee
nwwwsewwnewwse
ewenwesweeseseeeeseseswnenwsesee
esewseswsesesenwnweseseesesenweenwe
swswwnenesewsewseneswneseswswneneseese
nenenwnenenwneswneswsenwenwnenenw
swneseseeswseswsewswsesewnwseswswnwsee
wswswswswnwewwswwswswwwsweewew
esweneesenenweeneweeeseeeneswne
nwenwseneswnwnwnwwswnwenwnwwwnwnwne
seswsweseswswswseswswswswneswnenwswswswsw
swnwswswnwseswnwwsese
wswneswswneswsewwswwesww
neweenewswswnesesenenesenenwe
swnwseswwseseneseseswsesewwnweesese
wenweweeneneeeneseeswenee
seneesweenweeeswesee
wswswswsesewneeseneswswswswwesesesw
neneneseswnenenenenenenenenenesenenenewnew
neneseenenewenenenenwnenenweneseenesw
seneewwwwswnwsewwwwwwwwswwsw
seeseeseswnwewewnwseesesesesesenese
wwnwwenwnwnwnwwnwswewnenwwenww
senweeeeeeeeeswnwenweswwee
eswwwewseseeswneseneseenwwenesese
swsenweseseswseswseswnesesenweseswwwswsw
nwnwneswsweneneneewneswewnenwneseeswnw
senwswsewseseneenewseswseseseesesee
nwwnwnweswswsesenwwnenwwswwneseweene
wsesweswswswswwswnwswnwnwneseswesww
nwnwnwnwnwwnwwnwsenw
swwwnwnwewwwnwswwsesweewwwwe
nwnwswswswnwnwseswenwnewwnwenwnwnwe
neeenwneneneeneweneneswswnenene
swswswswswseswsenwswswswseseswewneswswe
seseseswewseseswswnesenesesewnwsesesenw
sewseeseseseseseseenesewseseswsewsese
swswswnewswswswswwswswsweewswwnwesw
nwwnenwnwnwnwsenwnenwnwnesenenenwnwnww
nesweswwswwswswwswswswsw
nesenesesweeneewswseneeswnwnenwswenw
eseeseeeenweeseseneeeswse
wenwswwwnwnwnwenwwwwwwneswnwnw
ewseeeneeseseeneswwse
swswseseswswswneswseenwwswnewseswswenwe
nenewswesenwwseseswswseseenwsewswneswse
swswesesesesesenwsenesenwneseswsewseswsese
nenwnesewnwnwnwnwenwnwnwsenwnwnenenwnw
wwwswwwwnewwsenewsewwnwwswenw
newesewsewseeseneswseseswnwnewsesese
sweweseneseneswswnwnenwenwnwneswne
ewnwneeeneenwseswswnwnwnenwwwnesene
swnwswnewnweenwnwnenwnwnenenwsenwnenenwnw
nwnwnwnwwnewnwwnwnwwsenwnwneseswwnw
wsewwwnwwwwwwwwnwwsenewseww
nwwnewsenwnenwnwnenwsenwsenwwnenenenwse
nwswseswnwswsweswsewseswswseseswneswsesw
seewewsesesesesene
nwwswswswswswswwswenwswswewswswswsw
sesewwwwwnewwnewnewneswesewwswne
esewseweseneseseseswsenwsesesenesese
swwsewwsenwwnesenewneewnwwwww
nwnwnwnwneseswneneswsenesenwnwnw
swneenenwnwswenwnenwwsewnwnwswenenw
nwsewseswswenewseneseseeseeswwseneew
swswnenwswewswnwswneneswswweswswesw
swnewesewwwwwwsewneseewnwww
swswswswwswseneneewweswneswsewswne
sesenwsesesesenewswnweseseseeswsesesw
swswnwswswnweswnwswsweswswwseseswwnww
wswswneswseneenewnesenesewnenwnweew
nwesesweeeseeeseewwenweseee
nwsesenesewseswseswseneswwswswwesene
sesenwswsesesesewsesenwnesesenwseseswse
ewnwwswnenwnesenenwnenwneseeswneneswnene
eneswnewnenwneneswseneseswnenwene
wwewwwnwwwwnwwwnwswwwewsw
wnenwenwnwneneneswenenwneneswnwsenene
sewsenwnwnwwwewnwsewwwnenenwwwnw
nwnwnwnwnwnwwswnenewnwnwewwnwnwwse
wnwwewwnwnwnwnwnwwnwnwww
neseseseesesesesesesenwswwnesesesese
wnwnewnwwsewnewse
enwnenwneswnwnwnwnwnwswnenwnwnwnwnwsee
eeeeeeenwweeeesw
nwsesesenwwseseseswsesenenesesesesesese
wnwnwneneenesenwseswwseswnwwwwee
nwswneneneneenwneneenwwnenenenesenwnene
wnwwwwwnewsewwwwwwwnw
swnwnwsewnewwnwnenewwwwseswnenesw
swseswswswswswswswnwnewneswwswswwswswse
swwswswnwwwewwwswwneswwwnesw
nwnwnwwnenwnwnwnwnwnwnenesenw
wseswswnwwwwwesenwnwesesesenwnwnw
eenewenenesenenwe
wwwewnwwsewwwwwnwwwwwsew
sweswsweewseseswswswswnwswswseswwnwse
wswseswneeseswswswnewseswswswseenwswsw
newwsenewnwwwwwwnwwsenwseewww
nwnwnwneswnwnwwnwnwnwenwnwnwnwswenwsw
sweseswnwnwenwseswnwnweneneneswnwswnesew
nwenwwnwsenwnwnwenwnwnewswwnenwnwnwenw
newsweeswswnwnenweseweeneswneswnesw
neeneseeenwseesenewwsweswnwenene
nwnwswswwnwsewswwswseswsewswnwewwse
nwnwwnwnwnwsenwsenwnwnenwewnwnwwnwsw
nenwsweeewnwnwnenenenwnwnenenenewnenw
sewswwswsewnewnewswwnenewwwwse
nwsesesenwewseseseseseseseswnesw
ewwwwwwwwsewwwswswswnenwswwswne
nenwsenwnwsewnwnwwnwnwnwsesenwnwnwnwnwnw
nwesewseseseeseseseseeseeseene
seewswwwnwsewnenwnwnwnwsweneswnesene
swswewswswwwneswswwswswnwwnewseswswsw
enwnwswnwwwsenwwnwnwenwwwwnwww
eneneswnenenenwnwnwne
nenenenenenenenenenenesewnewnenenesenw
swsweseswswsenenwswswswswswnwseswswswswnw
senewwswnwswesewnenwnwsenweseswsee
senewnewnwseewwwwswseswnwewnesw
sesenwesewneeseseseseswsesewnwnwenw
eweeneeeseeseneswe
nenenenenenewneneneseneneneneee
wswwwewwneswwwwwww
wewnwwnenwswnwneneswwnwsenwnenwswenwse
ewseseeeseseweseneseeseesesewee
swswswnesweswsenwsesewseseswseswesesesw
seseeeeswneweenwseseesewnewee
nwseeneesweneeneswswwnwesweeeeenw
seneseswseseesenwswsesesenweneseewswne
swsweneswswswnwseswswnwswswswswswswsene
neswswwnwseeseswnwwswnewsenenenwswnese
nwneneswswwseneswsewnewwewwseenewnw
eswswswseseseseseswnwseseswsesesenwese
nwsewwsewnwwnwneeeweeswwwwswsene
nwnwnwnwnwenwwwnwnw
swswswswsweswswswweswnwsenwwswswswswsw
nenesenwnwnenenwnenene
nwnewswnwswnwnenwswneseneewswseeneswnee
enenwnwnweneswnenwnwneneswwnwnenewsw
seseseesesewsewseseseneseswnesenesese
nwwsenewnwnwwsewwnwwsenwsenenwnwnww
sewseseseseseseseseseenweseeswsenwse
wewsewwwswwewnwwswnwwneswsww
swwswswwswswwswwwneeswsw
nwenwswneesenenenwnwnwswwnwenesw
neeeswnwsesewenwsesweswwene
nenwswswnwneneneenwwnwenenwnewnwneeene
nwswswnenenwswwsesesw
nenwnesenwwnwnwnwnenenenenesesenwnwnwne
seseesewseeeeeesewesenenewsesesenw
swsesesewwsenweeswswnenweswesenwnwsw
nwseseeseseswsenwseseseswswseseswwsesw
nenwswwswswswwswswswswewswwnewsww
swswswswwswewseswneswswswneseswswseswsw
swnwnwnwnwnwnwnwnwnwnwnwnwswnwenwenwnw
nesweseswesenwwsweswswnwsewswwswsw
senenwwwwswwswnwwenesw
nwesewnwnwnwnwwnweseenwnwwnwnwsww
swesenewnwneswseeswsewnwneswneswwsw
sesesesenwsewsesesesesesewsenesesenese
seeseewswswwswneenwsww
wnenwnewenwnwneeneneseswseeneenwesesw
nwenwnwswnwnwwwnwwwwnw
neswwwwswwsenwswseweswwwnweww
sesweeeeeswnwenwee
neseseswneseswseeswsewseseswsenwseseswswse
swnwnwnwnwnwwnwwnwnenwwnwwnw
eseeeseeeneeeneseeeweeewe
eeeswneeweswneeenwewsweswene
sewwwnwnwwenwsenwwwnenwnwwwnwww
seneseneswseswswswnwswseseswswwswswswsw
swnwwwwwwwnwwswseseswwneswswsww
nwnewnenenenwnwsenweenwwnewneeswne
wwewnewwsenwnenewsewwwsewswnwsew
nwnwnenwswnwnwneswwnwswnwwnenwswnwnwee
eeeesweeeewswneeeneeeeee
eeseeseweeeseeseeenesese
nwswnwswneneneneneneswnenenenewnwese
seseseeswseswsesesenesenwsewswsesenwsesese
wsewseswseenesenwseseseneswsewesewe
enweeneseeneenewswseneenewene
nenwsesenwnwsewnwnwnwwwnwwwswnwnwwne
seseswseseseseseseneseneesewse
neeneeneneenenwswneneneswnesenenewnene
swnwenwnwnwneswnwswnenwnwnw
eeswnwneeneeenee
neseseenwsewsewswseneeswswseeenesesee
swwnwnwnwneswnwnenwnwsenwnenenwse
nwnwnwewswwsweseswswsenwwswsewenw
nwnwewswnwsenwsewswwswwwswe
wswwwwwwewwwwww
wnwswwswwwswnenwwewsewwwswsewsw
eneneeenenenenewseneneswneenenewnesene
wsenwnwwnwnwswenwnwnwswnwwnwnwnenwnwnese
senewnwswsenwseswsenwseseeenew
wnwnwnwwwnwwenwnwnwnwnw
sweewwwneswwwnweeswnwenwwwwenw
swnwnwnwnewwnwnwwnwnwnwsenwne
enwswnwnwsenenesenwswnweswnesesenwwnenww
nenwnwnwsewnwnwnenwnwnwnw
nenenenenwnenwwneswsesenenewnenenenenese
neneenenenwneseenwwnwnenenenenewnwnw
neneneeneweenenenenewseneswse
seseneswsesesesesesewseseseswesenenesese
seeseneseswsenwswseswneesesesewswnwnwwse
seeeeseeeeseeeseeswwnenewsee
senwnwnwnwwneswswnwwnweenwnwnwwnwnw
wswswnwswswwswsweeswsesweswswsenew
senwnwnenwwnwnwnwnwswnwenesenwnwnwne
senwnwnwnesenwnwneenwneweeswnwnwswnw
nwwnwwwsewsewwwswenwnwe
eswnenenenenwneneneneneeeenee
swneewseseenenenweeneeeeeenee
senwwneseesewwseswnwswnewnw
enwwwwwsenwwnwwwswwwwwewww
nwswswwsenwnwnwnwwwnwwnwneesewnwnwne
nwnesesewsewswnwsesewnwneeeswwswese
esesewnewwnesenwwnwseswne
wnwwwwnewnewnewnwnwsenwswwseww
sesewseseseswswswsesweswseesenww
eewenenweneseeeeswswenwwe
neswweneneweeneneenwneeswseeneese
neseseswseseseesenwnwsesesesewewsese
wnwnenwseewswnwwwnwnwe
seeswnwewwswewnwnwwnwenwswswnw
swseneswneseseseseseseswseswnwswsesewsw
neseeewesenwnwwneneseeweswseswnw
nenweenenweeseeeeeeswnweeeswsene
eseseseeenweesesesweeese
seneseswwwsenwnesewneseseseesew
esweeeeeeeneeeeenw
nenwwwwswnwnwnesenwwnwnwnwsenenw
nwenwnwnesenwnwnwneswwwnwsenwwwnwww
wewswseseswneseswneswseswnweseneww
ewnwnewwwsewnwwswswnwwwwnwwewnw
nwseswnwnwnwsesenwnwsesenwneneneneseewsw
wnwnwwnwnwnwnwwwnwwwwew
wnwwnwnwsenwnwnwwnwnwwne
nenwnwswnewneewswseneeenenwnenenwe
nenwnwnwneneneneswwnwswsenenwesenwnenw
nwnwnwewwnwwnewwnwswwwwwneswnwse
enwnwseseseswsweewnwnwsesesesenewsene
nenesenenwneenenenenewnewsewneenwswne
swweswwswswnwswswwwswswswsw
nwsesweswseseswseswnenwswsenwnesewnw
wwwswswswwswnewswswwsewswwnenww"""


test1 = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""
test2 = """nwwswee"""
test3 = """"""
test4 = """"""



look = {"w":(-1,1,0), "e":(1,-1,0), "sw":(0,1,-1), "se":(1,0,-1), "ne":(0,-1,1), "nw":(-1,0,1)}

def solve(data):
    global look
    lines = [i for i in data.splitlines()]


    start = (0,0,0)
    flipped = defaultdict(int)




    for line in lines:
        line = list(line)
        cur = ""
        start = (0,0,0)
        while line:
            cur += line.pop(0)

            if cur in look.keys():
                print(cur, start, look[cur])
                start = (start[0]+look[cur][0], start[1]+look[cur][1], start[2]+look[cur][2])
                cur = ""

        print(start)
        flipped[start] = 1-flipped[start]

    tot = 0
    for j in flipped:
        #print(j, flipped[j])
        tot += flipped[j]


    for i in range(100):
        flipped = sim(flipped)
        tot = 0
        for j in flipped:
            tot += flipped[j]
        print(i+1, tot)



def sim(grid):
    global look
    doing = set()

    for x,y,z in grid.keys():
        doing.add((x,y,z))
        for dx,dy,dz in look.values():
            nx, ny, nz = x+dx, y+dy, z+dz
            doing.add((nx, ny, nz))

    new = defaultdict(int)

    for x,y,z in doing:

        adj = [grid[(x+dx, y+dy, z+dz)] for dx,dy,dz in look.values()]

        if grid[(x, y,z)]==1:
            if adj.count(1)==0 or adj.count(1) > 2:
                new[(x, y,z)] = 0
            else:
                new[(x,y,z)] = 1
        else:
            if adj.count(1)==2:
                new[(x,y,z)] = 1
            else:
                new[(x,y,z)] = 0
    return new









#solve(test1)
#solve(test2)
#solve(test3)
#solve(test4)

solve(data)






