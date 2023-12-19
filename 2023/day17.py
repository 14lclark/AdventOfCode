a = 'day17.txt'
# a = 'day17test.txt'

with open(a) as f:
    txt = [list(map(int, list(x))) for x in f.read().strip('\n').split()]
    
left = (-1, 0)
right = (1, 0)
up = (0, -1)
down = (0, 1)

dirs = [left, right, up, down]

dot = lambda x, y: x[0] * y[0] + x[1] * y[1]
add = lambda x, y: (x[0] + y[0], x[1] + y[1])
mul = lambda c, x: (c * x[0], c * x[1])
sub = lambda x, y: add(x, mul(-1, y))
def nbrs(x, y, nodiagonal = True):
    out = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i==0 and j==0:
                continue
            if nodiagonal and (i==j or i==-j):
                continue
            out.append((x+i, y+j))
    return out

def legal_index(v, maxx, maxy) :
    x, y = v
    return 0 <= x <= maxx and 0 <= y <= maxy

from math import inf
from itertools import product
graph = {}
graph2 = {}
for p in product(range(len(txt[0])), range(len(txt))): 
    for lastdir in dirs:
        graph[(p, lastdir)] = list()
        graph2[(p, lastdir)] = list()
        for nextdir in dirs:
            if dot(nextdir, lastdir) != 0: #nextdir[0] == lastdir[0] or nextdir[1] == lastdir[1]:
                continue
            total_weight = 0
            start = p
            for k in range(10):
                start = add(start, nextdir)
                if k < 3:
                    if legal_index(start, len(txt[0])-1, len(txt)-1):
                        total_weight += txt[start[1]][start[0]]
                        if ((start,nextdir), total_weight) not in graph[(p, lastdir)]:
                            graph[(p, lastdir)].append(((start,nextdir), total_weight))
                if k >= 3:
                    if legal_index(start, len(txt[0])-1, len(txt)-1):
                        total_weight += txt[start[1]][start[0]]
                        if ((start,nextdir), total_weight) not in graph2[(p, lastdir)]:
                            graph2[(p, lastdir)].append(((start,nextdir), total_weight))

# print(graph)
import heapq

def dijkstra(gr, start):
    print("starting dijkstra")
    heap = [(0, start)]
    heapq.heapify(heap)
    dist = {a: inf for a in gr.keys()}
    prev = {a: None for a in gr.keys()}
    dist[start] = 0

    while len(heap):
        d, u = heapq.heappop(heap)
        for v, weight in gr[u]:
            alt = d + weight
            if alt < dist[v]:
                if (dist[v], v) in heap:
                    heap.remove((dist[v], v))
                dist[v] = alt
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))
    return dist, prev

# [(((0, 6), (0, -1)), 4), (((0, 5), (0, -1)), 5), (((0, 4), (0, -1)), 9), (((0, 6), (0, -1)), 4), (((0, 5), (0, -1)), 5), (((0, 4), (0, -1)), 9)]

start = ((0,0), right)
end = (len(txt[0])-1, len(txt)-1)
d, p = dijkstra(graph, start)
print(d[(end, right)])
print(d[(end, down)])

start = ((0,0), down)
end = (len(txt[0])-1, len(txt)-1)
d, p = dijkstra(graph, start)
print(d[(end, right)])
print(d[(end, down)])

# part two
print('part 2')

start = ((0,0), right)
end = (len(txt[0])-1, len(txt)-1)
d, p = dijkstra(graph2, start)
print(d[(end, right)])
print(d[(end, down)])

start = ((0,0), down)
end = (len(txt[0])-1, len(txt)-1)
d, p = dijkstra(graph2, start)
print(d[(end, right)])
print(d[(end, down)])


# print(p)

# show = [["" for _ in range(len(txt[0]))] for _ in range(len(txt))]
# for i,j in d:
#     show[j][i] = d[(i,j)]
# for x in show:
#     print(x)
# show = [[" " for _ in range(len(txt[0]))] for _ in range(len(txt))]
# # print()
# # # print(p)
# print(d[(end, right)])
# print(d[(end, down)])

# pt = (end, right)
# while pt != start:
#     # print(pt)
#     i,j = pt[0]
#     show[j][i] = str(txt[j][i])
#     pt = p[pt]
# show[0][0] = "S"
# print('\n'.join([''.join(x) for x in show]))

# show = [[" " for _ in range(len(txt[0]))] for _ in range(len(txt))]
# print()
# # # print(p)
# pt = (end, down)
# while pt != start:
#     # print(pt)
#     i,j = pt[0]
#     show[j][i] = str(txt[j][i])
#     pt = p[pt]
# show[0][0] = "S"
# print('\n'.join([''.join(x) for x in show]))
# print()
# print()
# print('\n'.join([''.join(x) for x in show]))
# print('\n'.join([''.join(x) for x in [map(str,x) for x in txt]]))
# show = [[" " for _ in range(len(txt[0]))] for _ in range(len(txt))]
# print()
# print(p)
# pt = end
# while pt != start:
#     # print(pt)
#     i,j = pt
#     show[j][i] = str(s[(i,j)])
#     pt = p[pt]
# show[0][0] = "S"
# print()
# print()
# print('\n'.join([''.join(x) for x in show]))
        
# print(d)
# print(d[(end, right)])
# print(d[(end, down)])

# print(d)
# print()
# print(p)
# su = 0
# curr = end
# while curr != start:
#     print(curr, s[curr], txt[curr[1]][curr[0]])
#     curr = p[curr]
#     su += txt[curr[1]][curr[0]]
# print(curr)
