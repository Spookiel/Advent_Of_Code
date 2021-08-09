from collections import deque, Counter, defaultdict
import re

data=  """59750939545604170490448806904053996019334767199634549908834775721405739596861952646254979483184471162036292390420794027064363954885147560867913605882489622487048479055396272724159301464058399346811328233322326527416513041769256881220146486963575598109803656565965629866620042497176335792972212552985666620566167342140228123108131419565738662203188342087202064894410035696740418174710212851654722274533332525489527010152875822730659946962403568074408253218880547715921491803133272403027533886903982268040703808320401476923037465500423410637688454817997420944672193747192363987753459196311580461975618629750912028908140713295213305315022251918307904937"""
test = """03036732577212944063491565474664"""



def get_base(pos):
    base = [0, 1, 0, -1]
    for i in range(len(base)):
        base[i] = [base[i] for _ in range(pos)]
    new = []
    for t in base:
        for m in t:
            new.append(m)
    return new

def step(string):
    new = []
    start = True
    for i in range(len(string)):
        tot = 0
        pat = get_base(i+1)
        patpos = 1
        for j in range(len(string)):
            tot += int(string[j])*pat[patpos%len(pat)]
            patpos += 1

        new.append(str(tot)[-1])
    return new


def step2(string):
    new = []
    start = True
    for i in range(len(string)):
        tot = 0
        pat = get_base(i+1)
        patpos = 1
        for j in range(len(string)):
            tot += int(string[j])*pat[patpos%len(pat)]
            patpos += 1
        tot *= 10000
        new.append(str(tot)[-1])
    return new

def part2(string):
    offset = string[:7]
    print(offset)
    offset = int(offset)
    for _ in range(100):
        string = step2(string)
    print((string*10000)[offset-1:offset+7])


def solve(data, ph):
    pattern = r"-?\d+"
    base = [0, 1, 0, -1]

    data = [i for i in data]
    for _ in range(ph):
        print(_)
        data = step(data)
    print("".join(data[:8]), "ANSWER")


input_string = data
offset = int(input_string[:7], 10)
input_list = list(map(int, input_string)) * 10000
input_length = len(input_list)

for i in range(100):
    partial_sum = sum(input_list[j] for j in range(offset, input_length))
    for j in range(offset, input_length):
        t = partial_sum
        partial_sum -= input_list[j]
        if t >= 0:
            input_list[j] = t % 10
        else:
            input_list[j] = (-t) % 10

print(input_list[offset: offset + 8])