import re

data = """3,8,1001,8,10,8,105,1,0,0,21,42,67,76,89,110,191,272,353,434,99999,3,9,102,2,9,9,1001,9,2,9,1002,9,2,9,1001,9,2,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,101,3,9,9,1002,9,2,9,1001,9,4,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,1001,9,3,9,1002,9,3,9,4,9,99,3,9,102,3,9,9,101,2,9,9,1002,9,3,9,101,5,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99"""




def mode(mode, pos, lines):
    if mode == 1:
        return lines[pos]
    return int(lines[int(lines[pos])])


def find_both_modes(lines, n, last):
    #lines = [int(i) for i in lines.split(",")]

    # Utility function
    def mode(mode, pos, lines):
        if mode == 1:
            return lines[pos]
        return int(lines[int(lines[pos])])
    ans = [n].extend([last])
    pos = 0
    while pos < len(lines):
        code = str(lines[pos])[-2:]
        params = [0, 0, 0]
        if len(str(lines[pos])) > 1:
            if int(code) not in [3, 4]:
                for i in range(-3, (len(str(lines[pos])) * -1) - 1, -1):
                    if str(lines[pos])[i] == "1":
                        params[i + 2] = 1
                params = params[::-1]
        if int(code) == 99:
            raise StopIteration()
        if int(code) == 1:
            lines[lines[pos + 3]] = mode(params[0], pos + 1, lines) + mode(params[1], pos + 2, lines)
            pos += 4
        elif int(code) == 2:
            lines[lines[pos + 3]] = mode(params[0], pos + 1, lines) * mode(params[1], pos + 2, lines)
            pos += 4
        elif int(code) == 3:
            lines[lines[pos + 1]] = ans.pop(0)
            pos += 2
        elif int(code) == 4:
            ans.append(lines[lines[pos + 1]])
            pos += 2
        elif int(code) == 5:
            if mode(params[0], pos + 1, lines) > 0:
                pos = mode(params[1], pos + 2, lines)
            else:
                pos += 3
        elif int(code) == 6:
            if mode(params[0], pos + 1, lines) == 0:
                pos = mode(params[1], pos + 2, lines)
            else:
                pos += 3
        elif int(code) == 7:
            if mode(params[0], pos + 1, lines) < mode(params[1], pos + 2, lines):
                lines[lines[pos + 3]] = 1
            else:
                lines[lines[pos + 3]] = 0
            pos += 4
        elif int(code) == 8:
            if mode(params[0], pos + 1, lines) == mode(params[1], pos + 2, lines):
                lines[lines[pos + 3]] = 1
            else:
                lines[lines[pos + 3]] = 0
            pos += 4
    return ans

test = """3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"""

def comp(nums, program):
    return 0


from itertools import combinations
def solve(data):
    program = list(map(int, data.split(",")))
    m = -999
    for a in range(5,10):
        for b in range(5,10):
            for c in range(5,10):
                for d in range(5,10):
                    for e in range(5,10):
                        s = [a, b, c, d, e]
                        if len(set(s))==5:
                            ans = comp(s, program)
                            if ans > m:
                                m = ans
                                print(m, s)

solve(data)

data2 = "3,8,1001,8,10,8,105,1,0,0,21,38,63,88,97,118,199,280,361,442,99999,3,9,1002,9,3,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,101,3,9,9,102,5,9,9,101,3,9,9,1002,9,3,9,101,3,9,9,4,9,99,3,9,1002,9,2,9,1001,9,3,9,102,3,9,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,102,4,9,9,101,5,9,9,102,2,9,9,101,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99".split(",")
data2 = "3,8,1001,8,10,8,105,1,0,0,21,38,55,68,93,118,199,280,361,442,99999,3,9,1002,9,2,9,101,5,9,9,102,4,9,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,1001,9,4,9,4,9,99,3,9,101,4,9,9,102,3,9,9,4,9,99,3,9,102,2,9,9,101,4,9,9,102,2,9,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,1002,9,2,9,1001,9,2,9,1002,9,5,9,1001,9,2,9,1002,9,4,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99".split(",")
data = []

for i in range(len(data2)):
    data.append(int(data2[i]))


OP = [int(x) for x in  data]

def get_args(P, ip, n, digits, output):
    while len(digits) < n:
        digits = [0]+digits
    ans = P[ip+1:ip+n+1]
    if output:
        assert digits[0] == 0
        digits[0] = 1
    ans = [x if digits[len(digits)-1-i]==1 else P[x] for i,x in enumerate(ans)]
    return ans

def perms(A):
    if len(A) == 0:
        return [[]]
    ans = []
    for i,x in enumerate(A):
        A2 = A[:i]+A[i+1:]
        B2 = perms(A2)
        for b in B2:
            ans.append([x]+b)
    return ans
PERM = perms([5,6,7,8,9])

def run(inputs,ip):
    P = [x for x in OP]
    while True:
        digits = [int(x) for x in str(P[ip])]
        opcode = (0 if len(digits)==1 else digits[-2])*10+digits[-1]
        digits = digits[:-2]
        if opcode == 1:
            i1,i2,i3 = get_args(P, ip, 3, digits, True)
            P[i3] = i1+i2
            ip += 4
        elif opcode == 2:
            i1,i2,i3 = get_args(P, ip, 3, digits, True)
            P[i3] = i1*i2
            ip += 4
        elif opcode == 3:
            i1 = P[ip+1]
            P[i1] = inputs[0]
            inputs.pop(0)
            ip += 2
        elif opcode == 4:
            i1 = P[ip+1]
            ip += 2
            return P[i1],ip
        elif opcode == 5:
            i1,i2 = get_args(P, ip, 2, digits, False)
            if i1!=0:
                ip = i2
            else:
                ip += 3
        elif opcode == 6:
            i1,i2 = get_args(P, ip, 2, digits, False)
            if i1==0:
                ip = i2
            else:
                ip += 3
        elif opcode == 7:
            i1,i2,i3 = get_args(P, ip, 3, digits, True)
            if i1 < i2:
                P[i3] = 1
            else:
                P[i3] = 0
            ip += 4
        elif opcode == 8:
            i1,i2,i3 = get_args(P, ip, 3, digits, True)
            if i1 == i2:
                P[i3] = 1
            else:
                P[i3] = 0
            ip += 4
        else:
            assert opcode == 99, opcode
            return None, ip
print(data[295], "here")
ans = 0
for perm in PERM:
    val = 0
    IP = [0 for _ in range(len(perm))]
    VAL = [0 for _ in range(len(perm))]
    Q = [[perm[i]] for i in range(len(perm))]
    Q[0].append(0)
    done = False
    while not done:
        for i in range(len(perm)):
            val,new_ip = run(Q[i], IP[i])
            if val == None:
                print(perm,VAL[-1])
                if VAL[-1] > ans:
                    ans = VAL[-1]
                done = True
                break
            IP[i] = new_ip
            if val != None:
                VAL[i] = val
            Q[(i+1)%len(Q)].append(val)
            #print(i,val,new_ip,OP[new_ip])
print(ans)
