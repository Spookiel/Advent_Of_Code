from itertools import permutations

data2 = "3,8,1001,8,10,8,105,1,0,0,21,38,63,88,97,118,199,280,361,442,99999,3,9,1002,9,3,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,101,3,9,9,102,5,9,9,101,3,9,9,1002,9,3,9,101,3,9,9,4,9,99,3,9,1002,9,2,9,1001,9,3,9,102,3,9,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,102,4,9,9,101,5,9,9,102,2,9,9,101,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99".split(",")
data = []

for i in range(len(data2)):
    data.append(int(data2[i]))

def computer(data,input1,input2, programCounter=0):
    print(input1, input2, programCounter)
    i = programCounter
    numInputs = 0
    while i <= len(data):
        print(data[i])
        instruction = ""
        for g in range(len(str(data[i]))):
            instruction = list(str(data[i]))
        while len(instruction) != 5:
            instruction.insert(0,'0')
        inst = int(instruction.pop(-2)+instruction.pop(-1))
        for j in range(len(instruction)):
            instruction[j] = int(instruction[j])
        if inst == 1:
            if instruction[-1] == 0:
                if instruction[-2] == 0:
                    data[data[int(i+3)]] = int(data[int(data[i + 2])]) + int(data[int(data[i+1])])
                else:
                    data[data[i + 3]] = data[i + 2] + data[int(data[i+1])]
            else:
                if instruction[-2] == 0:
                    data[data[i + 3]] = data[int(data[i + 2])] + data[i+1]
                else:
                    data[data[i + 3]] = data[i + 2] + data[i+1]
            i += 4
        elif inst == 2:
            if instruction[-1] == 0:
                if instruction[-2] == 0:
                    data[data[i + 3]] = data[int(data[i + 2])] * int(data[int(data[i + 1])])
                else:
                    data[data[i + 3]] = data[i + 2] * int(data[int(data[i + 1])])
            else:
                if instruction[-2] == 0:
                    data[data[i + 3]] = data[int(data[i + 2])] * int(data[i + 1])
                else:
                    data[data[i + 3]] = data[i + 2] * int(data[i + 1])
            i += 4
        if inst == 3:
            if numInputs == 0:
                data[int(data[i+1])] = input1
            else:
                data[int(data[i + 1])] = input2
            i += 2
            numInputs += 1
        if inst == 4:
            i += 2
            return (i, data[int(data[i-1])], data)
        if inst == 5:
            if instruction[-1] == 0:
                if data[data[i + 1]] != 0:
                    if instruction[-2] == 0:
                        i = data[data[i + 2]]
                    else:
                        i = data[i + 2]
                else:
                    i += 3
            else:
                if data[i + 1] != 0:
                    if instruction[-2] == 0:
                        i = data[data[i + 2]]
                    else:
                        i = data[i + 2]
                else:
                    i += 3
        if inst == 6:
            if instruction[-1] == 0:
                if data[data[i + 1]] == 0:
                    if instruction[-2] == 0:
                        i = data[data[i + 2]]
                    else:
                        i = data[i+2]
                else:
                    i += 3
            else:
                if data[i+1] == 0:
                    if instruction[-2] == 0:
                        i = data[data[i+2]]
                    else:
                        i = data[i+2]
                else:
                    i += 3
        if inst == 7:
            if instruction[-1] == 0:
                if instruction[-2] == 0:
                    if data[data[i+1]] < data[data[i+2]]:
                        data[data[i+3]] = 1
                    else:
                        data[data[i+3]] = 0
                else:
                    if data[data[i+1]] < data[i+2]:
                        data[data[i+3]] = 1
                    else:
                        data[data[i+3]] = 0
            else:
                if instruction[-2] == 0:
                    if data[i+1] < data[data[i+2]]:
                        data[data[i+3]] = 1
                    else:
                        data[data[i+3]] = 0
                else:
                    if data[i+1] < data[i+2]:
                        data[data[i+3]] = 1
                    else:
                        data[data[i+3]] = 0
            i += 4
        if inst == 8:
            if instruction[-1] == 0:
                if instruction[-2] == 0:
                    if data[data[i+1]] == data[data[i+2]]:
                        data[data[i+3]] = 1
                    else:
                        data[data[i+3]] = 0
                else:
                    if data[data[i+1]] == data[i+2]:
                        data[data[i+3]] = 1
                    else:
                        data[data[i+3]] = 0
            else:
                if instruction[-2] == 0:
                    if data[i+1] == data[data[i+2]]:
                        data[data[i+3]] = 1
                    else:
                        data[data[i+3]] = 0
                else:
                    if data[i+1] == data[i+2]:
                        data[data[i+3]] = 1
                    else:
                        data[data[i+3]] = 0
            i += 4
        elif inst == 99:
            return None

perm = list(permutations([5,6,7,8,9]))

maxOutput = -10000000
from copy import deepcopy
#data = """3,8,1001,8,10,8,105,1,0,0,21,42,67,76,89,110,191,272,353,434,99999,3,9,102,2,9,9,1001,9,2,9,1002,9,2,9,1001,9,2,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,101,3,9,9,1002,9,2,9,1001,9,4,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,1001,9,3,9,1002,9,3,9,4,9,99,3,9,102,3,9,9,101,2,9,9,1002,9,3,9,101,5,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99"""
#data = [int(i) for i in data.split(",")]
for i in list(perm):
    count = 0
    a = i[0]
    b = i[1]
    c = i[2]
    d = i[3]
    e = i[4]
    input1 = 0
    print(i, maxOutput)
    flag = False

    # This is the main loop
    outs = [None, None, None, None, 0]
    positions = [[0, deepcopy(data)], [0, deepcopy(data)], [0, deepcopy(data)], [0, deepcopy(data)],
                 [0, deepcopy(data)]]
    while True:

        #This is one iteration, but not quite because E does not feed back into A
        for j in range(5):
            new = computer(positions[j][1], i[j], outs[(j-1)%5], positions[j][0])
            #New returns positions, signal, data
            if new is None:
                print(outs[-1])
                flag = True
                break
            else:
                positions[j][0], outs[j], positions[j][1] = new
        print(outs)
        input()

        if flag:
            if outs[-1] > maxOutput:
                maxOutput = outs[-1]
                break


print(maxOutput)

#The way I thought about it is, we need to run one of the programs until it gives us an output value, or E gives the stop code
#Therefore we need to stop and start each program, based on where the program counter is
#