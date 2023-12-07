with open("day7.txt") as f:
    txt = [x.strip().split(" ") for x in f.read().strip().split("\n")]

hands = [(x[0], int(x[1])) for x in txt]

cardorder = '23456789TJQKA'
cardscore = dict(zip(cardorder, range(len(cardorder))))

def toscores(hand):
    return [cardscore[x] for x in hand]

def count(s):
    c = {}
    for i in s:
        if i in c:
            c[i] += 1
        else:
            c[i] = 1
    return c

def _lt(hand1, hand2):
    c1 = count(hand1)
    c2 = count(hand2)
    hand1 = toscores(hand1)
    hand2 = toscores(hand2)
    if len(c1) != len(c2):
        return len(c1) > len(c2)
    if len(c1) == len(c2) and (sorted(c1.values()) != sorted(c2.values())):
        return max(c1.values()) < max(c2.values())

    def one_by_one(h1, h2):
        if len(h1) == 1:
            return h1[0] < h2[0]
        if h1[0] == h2[0]:
            return one_by_one(h1[1:], h2[1:])
        return h1[0] < h2[0]
    return one_by_one(hand1, hand2)

class K:
    def __init__(self, hand):
        self.hand = hand
    def __lt__(self, other):
        return _lt(self.hand[0], other.hand[0])

ranks = sorted(hands, key=K)
s = 0
for i, (_, bid) in enumerate(ranks):
    s += (i+1) * bid
print(s)
