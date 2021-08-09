data = """deal with increment 66
cut -2068
deal with increment 8
cut -6565
deal with increment 22
cut -8629
deal with increment 56
cut -697
deal with increment 58
cut 4957
deal with increment 71
cut -4506
deal with increment 39
cut 6144
deal with increment 48
cut 1392
deal with increment 51
cut -8043
deal with increment 30
cut 7798
deal with increment 25
deal into new stack
deal with increment 43
cut 1048
deal with increment 63
cut 257
deal into new stack
deal with increment 15
deal into new stack
deal with increment 12
deal into new stack
cut 3316
deal with increment 68
cut -4495
deal with increment 4
cut -421
deal with increment 11
cut 7629
deal with increment 32
cut -3956
deal with increment 33
cut -596
deal with increment 42
cut 8505
deal into new stack
cut 4215
deal with increment 74
cut 9999
deal with increment 7
deal into new stack
deal with increment 71
cut 6836
deal with increment 27
cut 188
deal with increment 45
deal into new stack
deal with increment 17
cut -6659
deal into new stack
cut -8919
deal with increment 23
cut 7758
deal with increment 58
cut -9377
deal with increment 51
cut -8010
deal into new stack
cut -8058
deal with increment 57
deal into new stack
deal with increment 7
cut -1977
deal into new stack
cut -4748
deal with increment 55
cut -2901
deal into new stack
cut 4362
deal with increment 65
cut -4367
deal with increment 51
cut 2133
deal into new stack
deal with increment 15
deal into new stack
deal with increment 28
cut -5331
deal with increment 41
cut -5157
deal with increment 68
cut 4776
deal into new stack
deal with increment 28
cut 2005
deal with increment 14
deal into new stack
cut 1341
deal into new stack
cut 7623
deal with increment 36"""



test = """deal with increment 7
deal into new stack
deal into new stack"""


from collections import deque
def deal_stack(cards):
    new = deque()
    while len(cards) > 0:
        new.appendleft(cards.popleft())
    return new

def cut(cards, n):
    if n > 0:
        for c in range(n):
            cards.append(cards.popleft())
    else:
        for c in range(0, n, -1):
            cards.appendleft(cards.pop())

    return cards

def deal_increment(cards,n):
    blank = [None for _ in range(len(cards))]
    pos = 0
    while len(cards) > 0:
        blank[pos%len(blank)] = cards.popleft()
        pos += n
    return deque(blank)


t = "0 1 2 3 4 5 6 7 8 9"
t = list(map(int, t.split()))
t = deque(t)
print(deal_increment(t, 3))


def solve(data):
    lines = [i for i in data.splitlines()]
    if len(lines) > 20:
        cards = deque([i for i in range(10007)])
    else:
        cards = deque([i for i in range(10)])
    for _ in range(1):
        print(_)
        for line in lines:
            line = line.split()
            if "increment" in line:
                cards = deal_increment(cards, int(line[-1]))
            elif "cut" in line:
                cards = cut(cards, int(line[-1]))
            else:
                cards = deal_stack(cards)
        print(cards)
    print(cards.index(2019))


solve(data)



with open('input.txt') as f:
    shuffle = f.read().strip().split('\n')

def part1(sz, shuf, p):
    # Find position of card p after shuffling deck of sz cards
    deck = list(range(sz))

    def cut(l, n):
        return l[n:] + l[:n]

    def deal_inc(l, inc):
        L=len(l)
        nl = [0]*L
        for i, x in enumerate(l):
            nl[(inc * i) % L] = x
        return nl

    for line in shuffle:
        if line.endswith("stack"):
            deck = deck[::-1]
            continue
        n = int(line.split()[-1])
        if line.startswith('cut'):
            deck = cut(deck, n)
        else:
            deck = deal_inc(deck, n)
    return deck.index(p)

print("Part 1:", part1(10007, shuffle, 2019))


def qemod(a, b, m):  # quick exponent a**b mod m
    if b==0: return 1
    if b%2:
        return (a*qemod((a**2)%m, b//2, m)) % m
    return qemod((a**2)%m, b//2, m)

def exeuclid(a,b):
    # d == gcd(a,b) == ax+by
    if b==0:
        return a,1,0  # a == gcd(a,0) == 1*a + 0*0
    d,x,y = exeuclid(b, a%b)
    return d, y, x - (a//b)*y

def modinv(a,b):
    # a**-1 mod b
    d,x,y = exeuclid(a,b)
    if d==1:
        return x%b
    return 0

def num_at_pos(sz, reps, shuf, p):
    # return (position of p, number at position p)
    # after shuffling the deck of 'sz' cards 'reps' times (with shuf)
    # We use that both are a linear function of p (second inverse of first):
    # if p1-p0=x then position of p after 1 rep is p0 + x*p  (mod sz)
    # and number at position p is (pos-p0) * (x**-1)  (mod sz)
    # rep 2: p0*(1 + x + x**2) + (x**2)(p-p0)
    p0 = 0
    p1 = 1
    for line in shuf:
        if line.endswith("stack"):
            # reverse: 0 => sz-1
            p0=~p0
            p1=~p1
            continue
        n = int(line.split()[-1])
        if line.startswith('cut'):
            p0-=n
            p1-=n
        else:
            p0*=n
            p1*=n
        p0%=sz
        p1%=sz
    x = (p1-p0)
    # Use the identity x^n+...+x^2+x+1 = (x^(n+1)-1)//(x-1)
    x_reps = qemod(x, reps, sz)
    #   p0 * (x^(n+1) -1) * ((x-1)**-1)
    dx = p0*((x_reps*x-1) * modinv(x-1, sz)) % sz
    pos_of_p = (dx + x_reps*(p-p0)) % sz
    # invert the permutation
    num_at_p = ((p-dx) * modinv(x_reps, sz) + p0) % sz
    return pos_of_p, num_at_p

print("Verify part 1:", num_at_pos(10007, 1, shuffle, 2019)[0])
print("Part 2:", num_at_pos(119315717514047, 101741582076661, shuffle, 2020)[1])














