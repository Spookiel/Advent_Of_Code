
import re
from collections import defaultdict, Counter
from itertools import permutations, combinations,product
from functools import lru_cache
adj4 = [[0,1], [1,0], [-1,0], [0,-1]]
adj8 = adj4+[[1,1], [-1,-1], [1,-1], [-1,1]]

def lmii(delim=" "):
    return list(map(int, input().split(delim)))

data = """1007125
13,x,x,41,x,x,x,x,x,x,x,x,x,569,x,29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,23,x,x,x,x,x,x,x,937,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,17"""


test1 = """939
7,13,x,x,59,x,31,19"""
test2 = """123
17,x,13,19"""
test3 = """"""
test4 = """"""
import math


def extended_euclidean(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_euclidean(b % a, a)
        return (g, x - (b // a) * y, y)

    # modular inverse driver function


def modinv(a, m):
    g, x, y = extended_euclidean(a, m)
    return x % m


# function implementing Chinese remainder theorem
# list m contains all the modulii
# list x contains the remainders of the equations
def crt(m, x):
    # We run this loop while the list of
    # remainders has length greater than 1
    while True:

        # temp1 will contain the new value
        # of A. which is calculated according
        # to the equation m1' * m1 * x0 + m0'
        # * m0 * x1
        temp1 = modinv(m[1], m[0]) * x[0] * m[1] + \
                modinv(m[0], m[1]) * x[1] * m[0]

        # temp2 contains the value of the modulus
        # in the new equation, which will be the
        # product of the modulii of the two
        # equations that we are combining
        temp2 = m[0] * m[1]

        # we then remove the first two elements
        # from the list of remainders, and replace
        # it with the remainder value, which will
        # be temp1 % temp2
        x.remove(x[0])
        x.remove(x[0])
        x = [temp1 % temp2] + x

        # we then remove the first two values from
        # the list of modulii as we no longer require
        # them and simply replace them with the new
        # modulii that  we calculated
        m.remove(m[0])
        m.remove(m[0])
        m = [temp2] + m

        # once the list has only one element left,
        # we can break as it will only  contain
        # the value of our final remainder
        if len(x) == 1:
            break

    # returns the remainder of the final equation
    return x[0]
def solve(data):

    lines = [i for i in data.splitlines()]

    targ = int(lines[0])
    bs = [i for i in lines[1].split(",")]
    ts = [(ind, int(bus)) for ind, bus in enumerate(bs) if bus!="x"]
    ns = [int(bus) for t, bus in ts]
    ass = [bus-t for t, bus in ts]
    print(ns, ass)

    print(crt(ns, ass))

solve(test1)
solve(test2)
#solve(test3)
#solve(test4)

solve(data)






