import re
#import networkx as nx
#from collections import defaultdict, Counter

data = """147981-691423"""

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
def solve(data):
    pattern = r"((\d)\2+)"
    lower, higher = list(map(int, data.split("-")))
    c = 0
    for num in range(lower, higher):
        if is_valid(num, pattern):
            c += 1
    print(c)


solve(data)