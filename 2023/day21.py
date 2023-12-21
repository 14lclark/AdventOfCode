a = 'day21.txt'
a = 'day21test.txt'
with open(a) as f:
    txt = [list(x) for x in f.read().strip().split('\n')]

from functools import cache
@cache
def nbrs(x, y, nodiagonal = True, mods=None):
    out = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i==0 and j==0:
                continue
            if nodiagonal and (i==j or i==-j):
                continue
            if mods is not None:
                out.append(((x+i) % mods[0], (y+j) % mods[1]))
                continue
            out.append((x+i, y+j))
    return out
is_legal = lambda x: x[0] in range(len(txt[0])) and x[1] in range(len(txt))

for j in range(len(txt)):
    for i in range(len(txt[0])):
        if txt[j][i] == "S":
            s = (i,j)
        
from collections import deque

def walk(start):
    g = [[start]]
    g = deque(g)
    for _ in range(64):
        g.append([])
        for x in g[-2]:
            nbr = [(i,j) for i,j in nbrs(*x) if is_legal(x) and txt[j][i] != "#" and (i,j) not in g[-1]]
            g[-1] += nbr
        g.popleft()
    return len(g[-1])





# print(walk(s))

width = len(txt[0])
height = len(txt)
start = {s: 0}
from collections import defaultdict
# global cache
# cache = [s]

global mycache
mycache = {}

@cache
def rnbrs(i,j):
    return [(i,j) for i,j in nbrs(i,j, mods=(width, height)) if txt[j][i] != "#"]

def walk2(prev):
    # if prev.keys() in mycache:
    #     new = 
    new = defaultdict(lambda: 0)
    for x in prev:
        nbs = rnbrs(*x)
        for nb in nbs:
            new[nb] += prev[x]
    return new

# for i in range(26501365):
for i in range(6):
    start = walk2(start)

print(len(s))