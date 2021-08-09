
data = """1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0"""
test = """2,3,0,3,99"""


def find(value1, value2, lines):
    lines[1] = value1
    lines[2] = value2
    pos = 0
    while pos < len(lines):
        new = lines[:]
        if lines[pos] == 99:
            break
        if lines[pos] == 1:
            new[lines[pos + 3]] = lines[lines[pos + 1]] + lines[lines[pos + 2]]
        elif lines[pos] == 2:
            new[lines[pos + 3]] = lines[lines[pos + 1]] * lines[lines[pos + 2]]
        pos += 4
        lines = new[:]
    return lines[0]

def solve(data):
    lines = [int(i) for i in data.split(",")]
    for a in range(100):
        for b in range(100):
            if find(a, b, lines)==19690720:
                print(a*100+b)
                break


solve(data)