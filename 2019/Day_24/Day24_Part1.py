data = """#..#.
.....
.#..#
.....
#.#.."""


test = """....#
#..#.
#..##
..#..
#...."""



def get(pos, board):
    found = []
    for move in [[0,1], [1,0], [0,-1], [-1,0]]:
        nx, ny = pos[0]+move[0], pos[1]+move[1]
        if nx >= 0 and ny >= 0:
            try:
                found.append(board[ny][nx])
            except:
                pass
    return found

def step(board):
    new  =[[None for i in range(5)] for j in range(5)]

    for i in range(len(board)):
        for j in range(len(board[0])):
            f = get((j, i), board)
            if board[i][j]=="#":
                if f.count("#")!=1:
                    new[i][j]="."
                else:
                    new[i][j] = "#"
            else:
                if f.count("#") in [1,2]:
                    new[i][j] = "#"
                else:
                    new[i][j] = "."
    return new

def calc(board):
    total = 0
    f = 1
    for i in board:
        for j in i:
            if j=="#":
                total += f
            f *= 2
    return total


found = set()
test = [[j for j in i] for i in data.splitlines()]
counter = 0
for i in range(1, 100000):
    a = calc(test)
    found.add(a)
    if len(found) != i:
        print("FOUND", a)
        for m in test:
            print(*m)
        break
    test = step(test)