import re
#import networkx as nx
#from collections import defaultdict, Counter

data = """"""

test = """"""

def is_increasing(num):
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            return False
    return True

def is_valid(num, pattern):
    for j in re.findall(pattern, str(num)):
        if is_increasing(str(num)):
            return True
        return False
    return False
pattern = r"((\d)\2+)"
print(is_valid("123444", pattern))
def solve():
    pattern = r"((\d)\2+)"
    c = 0
    for num in range(147981, 691423):
        if is_valid(num, pattern):
            c += 1
    print(c)
solve()