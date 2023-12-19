a = 'day18.txt'
# a = 'day18test.txt'
with open(a) as f:
    txt = [x.strip().split() for x in f.read().strip().split('\n')]

# print(txt)
txt = [(x[0],int(x[1]),x[2]) for x in txt]


dot = lambda x, y: x[0] * y[0] + x[1] * y[1]
add = lambda x, y: (x[0] + y[0], x[1] + y[1])
mul = lambda c, x: (c * x[0], c * x[1])
sub = lambda x, y: add(x, mul(-1, y))


locs = [(0,0)]
dirs = {"R": (1, 0), "L": (-1,0), "U": (0,1), "D": (0,-1) }
def dig(loc, instr):
    return add(loc, dirs[instr])

for instr in txt:

    for i in range(instr[1]):
        locs.append(dig(locs[-1], instr[0]))

minx, miny = min(locs, key=lambda x: x[0])[0], min(locs, key=lambda x: x[1])[1]
locs = [add((abs(minx), abs(miny)), loc) for loc in locs]
grid = [[" "  for _ in range(max(locs, key=lambda x: x[0])[0]+1)] for _ in range(max(locs, key=lambda x: x[1])[1]+1)]
peri = [[" "  for _ in range(max(locs, key=lambda x: x[0])[0]+1)] for _ in range(max(locs, key=lambda x: x[1])[1]+1)]
inside = [[" "  for _ in range(max(locs, key=lambda x: x[0])[0]+1)] for _ in range(max(locs, key=lambda x: x[1])[1]+1)]
maxx = len(grid[0])
maxy = len(grid)
for i, j in locs: 
   grid[j][i] = "#" 
   peri[j][i] = "#"


def neighbors(i, j, maxi, maxj):
    if i == 0: xs = [(i+1, j)]
    elif i == maxi: xs = [(i-1, j)]
    else: xs = [(i+1, j), (i-1, j)]
    if j == 0: ys = [(i, j+1)]
    elif j == maxj: ys = [(i, j-1)]
    else: ys = [(i, j+1), (i, j-1)]
    return xs + ys

nbs = [(0,0), (len(grid[0])-1, len(grid)-1), (0,len(grid)-1), (len(grid[0])-1, 0)]
while len(nbs) > 0:
    for x,y in nbs[:]:
        grid[y][x] = "O"
        for x1,y1 in neighbors(x,y,len(grid[0])-1,len(grid)-1):
            if (x1,y1) not in nbs and grid[y1][x1] == " ":
                nbs.append((x1,y1))
        nbs.remove((x,y))

nbs = [locs[-10]]
while len(nbs) > 0:
    for x,y in nbs[:]:
        grid[y][x] = "#"
        for x1,y1 in neighbors(x,y,len(grid[0])-1,len(grid)-1):
            if (x1,y1) not in nbs and grid[y1][x1] == " ":
                nbs.append((x1,y1))
        nbs.remove((x,y))



        line = ''.join(peri[j][i:]) 
        new = line.replace("###", "##")
        while new != new.replace("###", "##"):
            new = new.replace("###", "##")
        line = new
        num = line.count("#")
        if num % 2 == 1:
            inside[j][i] = "#"
            grid[j][i] =  "#"

x = sum([''.join(line).count("#") for line in grid])
print(x)
# with open('grid.txt', 'w') as f:
#     for line in [''.join(line) for line in grid]:
#         f.write(line + '\n')

# with open('peri.txt', 'w') as f:
#     for line in [''.join(line) for line in peri]:
#         f.write(line + '\n')

# part 2


tr = {0: "R", 1: "D", 2: "L", 3: "U"}
txt = [(tr[int(c[7])], int('0x' + c[2:7], base=16)) for _,_,c in txt]
# print(txt[:10])

def dig2(loc, dir, n):
    return add(loc, mul(n, dirs[dir]))

verts = [(0,0)]
for dir, n in txt: 
    # print(dir, n)
    verts.append(dig2(verts[-1], dir, n))

length = lambda x, y: abs(x[0] - y[0]) + abs(x[1]-y[1]) 

def perimeter(verts):
    s = 0
    for i in range(len(verts) - 1):
        s += length(verts[i], verts[i+1])
    return s


# Scan line ish attempt that I couldn't get to work properly.
# So I started looking for theorems :P

# horiz_lines = []
# vert_lines = []
# for i in range(len(verts)-1):
#     diff = sub(verts[i], verts[i+1])
#     for j in [0,1]:
#         if diff[j] != 0:
#             low, high = min(verts[i][j], verts[i+1][j]), max(verts[i][j], verts[i+1][j])
#             if j == 0:
#                 horiz_lines.append((range(low, high+1), verts[i][1]))
#                 # horiz_lines.append((range(low+1, high), verts[i][1]))
#             if j == 1:
#                 vert_lines.append((verts[i][0], range(low, high+1)))
        
# horiz_lines.sort(key=lambda x: x[1])
# xs,ys = list(map(list, zip(*verts)))
# xs = list(set(xs))
# xs.sort()
# print(xs)
# print(min(xs),min(ys))
# print(max(xs),max(ys))
# print(len(xs))
# s = 0
# filter_vert = lambda l: (lambda k: l[0] == k[0] and l[1] in k[1])
# for i in range(len(xs)-1):
#     hls = list(filter(lambda k: (xs[i]+1) in k[0][1:-1], horiz_lines))
#     print(xs[i])
#     print(hls) 
#     inside_width = (xs[i+1]-1) - (xs[i]+1) - 1
#     # f = lambda k: (xs[i]) in k[0] and (xs[i+1]) in k[0]
#     for j in range(0, len(hls), 2):
#         s += (hls[j+1][1] - hls[j][1] + 1) * (inside_width)

# for x in xs:
#     hls = list(filter(lambda k: (xs[i]) in k[0], horiz_lines))
#     print(x)
#     print(hls) 
#     # f = lambda k: (xs[i]) in k[0] and (xs[i+1]) in k[0]
#     for j in range(len(hls)-1):

#         s += (hls[j+1][1] - hls[j][1])
#     s += 1 

# # s += perimeter(verts)
# print(s)

def shoelace(verts):
    return 1/2 * abs(sum(x0*y1 - x1*y0 for ((x0, y0), (x1, y1)) in zip(verts, verts[1:] + [verts[0]])))
print(int(shoelace(verts) - perimeter(verts)/2 + 1 + perimeter(verts)))