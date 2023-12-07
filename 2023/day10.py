with open("day10.txt") as f:
    txt = [x for x in f.read().strip().split()]

tiles = {"L": [(1, 0), (0, -1)], "J": [(-1, 0), (0, -1)],
             "F": [(1, 0), (0, 1)], "7": [(-1, 0), (0, 1)],
            "|": [(0, 1), (0, -1)], "-": [(-1, 0), (1, 0)],
            "S": [(0,0)], ".": [(0,0)]}

s_ind = None
for j in range(len(txt)):
    for i in range(len(txt[0])):
        if txt[j][i] == "S":
            s_ind = (i,j)
            break
    else:
        continue
    break

def neighbors(i, j, maxi, maxj):
    if i == 0: xs = [(i+1, j)]
    elif i == maxi: xs = [(i-1, j)]
    else: xs = [(i+1, j), (i-1, j)]
    if j == 0: ys = [(i, j+1)]
    elif j == maxj: ys = [(i, j-1)]
    else: ys = [(i, j+1), (i, j-1)]
    return xs + ys

def add_tup(x,y):
    a, b = x
    c, d = y
    return (a+c, b+d)

loop = {True: [], False: []}
which = True
s_nb = neighbors(s_ind[0],s_ind[1], len(txt[0])-1, len(txt)-1)
for nb in s_nb:
    i,j = nb

    for x in tiles[txt[j][i]]:
        if add_tup(x, nb) == s_ind:
            loop[which].append(nb)
            which = not which

count = 0
while loop[True][-1] != loop[False][-1]:
    for x in [True, False]:
        curr = loop[x][-1]
        i,j = curr
        for dir in tiles[txt[j][i]]:
            next = add_tup(dir, curr)
            if next not in loop[x]:
                loop[x].append(next)
                count += 1
                break

print(count / 2)



s_angle = []
for x in [loop[True][0], loop[False][0]]:
    s_angle.append(add_tup(x, (-s_ind[0], -s_ind[1])))
print(s_angle)
for x in tiles:
    if set(tiles[x]) == set(s_angle):
        
        s = x
        print(s)
        break
# part 2

# determine what tile S is
loop = [x for x in set(loop[True]).union(set(loop[False]))]



mi = max(loop, key=lambda x: x[0])[0]
mj = max(loop, key=lambda x: x[1])[1]
parr = [["." for _ in range(len(txt[0]))] for _ in range(len(txt))]

for i,j in loop:
    parr[j][i] = txt[j][i]

i, j = s_ind
parr[j][i] = s

def sees_wall(i,j,arr,ch=" "):
    left, right, up, down = True, True, True, True
    for k in range(i)[::-1]:
        if arr[j][k] != ch:
            left = False
            break
    for k in range(i+1, len(arr[0])):
        if arr[j][k] != ch:
            right = False
            break
    for k in range(j)[::-1]:
        if arr[k][i] != ch:
            up = False
            break
    for k in range(j+1, len(arr)):
        if arr[k][i] != ch:
            down = False
            break
    return up or down or left or right

def sees_out(i,j,arr,out,ch=" "):
    for k in range(i)[::-1]:
        if arr[j][k] != ch:
            break
        if (k,j) in out:
            return True
    for k in range(i+1, len(arr[0])):
        if arr[j][k] != ch:
            break
        if (k,j) in out:
            return True
    for k in range(j)[::-1]:
        if arr[k][i] != ch:
            break
        if (i,k) in out:
            return True
    for k in range(j+1, len(arr)):
        if arr[k][i] != ch:
            break
        if (i,k) in out:
            return True
    return False
    



expanded = \
{"L":
'''
 x 
 xx
   
'''.strip("\n").split("\n"),
"J": 
'''
 x 
xx 
   
'''.strip("\n").split("\n"),
"F": 
'''
   
 xx
 x 
'''.strip("\n").split("\n"), 
"7": 
'''
   
xx 
 x 
'''.strip("\n").split("\n"),
"|": 
'''
 x 
 x 
 x 
'''.strip("\n").split("\n"),
 "-": 
'''
   
xxx
   
'''.strip("\n").split("\n"),
 ".":
'''
   
   
   
'''.strip("\n").split("\n"),
"O":
'''
OOO
OOO
OOO
'''.strip("\n").split("\n")}
     
def expand(arr, exp):
    new = [[" " for _ in range(3 * len(txt[0]))] for _ in range(3 * len(txt))]
    for j in range(len(arr)):
        for i in range(len(arr[0])):
            for y in range(3*j, 3*(j + 1)):
                for x in range(3*i, 3*(i+1)):
                    
                    new[y][x] = exp[arr[j][i]][y%3][x%3]
    return new

outside = []
for j in range(len(parr)):
    for i in range(len(parr[0])):
        if parr[j][i] != ".":
            continue
        if sees_out(i,j,parr,outside, ch="."):
            outside.append((i,j))
        if sees_wall(i,j,parr,ch="."):
            outside.append((i,j))
for i,j in outside:
    parr[j][i] = "O"

outside = []
for j in range(len(parr)):
    for i in range(len(parr[0])):
        if parr[j][i] != ".":
            continue
        if sees_out(i,j,parr,outside, ch="."):
            outside.append((i,j))

for i,j in outside:
    parr[j][i] = "O"

new = expand(parr, expanded)


with open("exp.txt", "w") as f:
    for i in new:
        f.write(''.join(i) + "\n")



for j in range(len(new)):
    for i in range(len(new[0])):
        if new[j][i] != "O":
            continue
        nbs = [(a,b) for a,b in neighbors(i,j,len(new[0])-1,len(new)-1) if new[b][a] == " "]
        while len(nbs) > 0:
            for x,y in nbs[:]:
                new[y][x] = "O"
                for x1,y1 in neighbors(x,y,len(new[0])-1,len(new)-1):
                    if (x1,y1) not in nbs and new[y1][x1] == " ":
                        nbs.append((x1,y1))
                nbs.remove((x,y))


for i,j in outside:
    new[j][i] = "O"

#reverse the expand 
for j in range(len(parr)):
    for i in range(len(parr[0])):
        old = parr[j][i]
        haso = False
        hasx = False
        for y in range(3*j, 3*(j + 1)):
            for x in range(3*i, 3*(i+1)):
                if new[y][x] == "O":
                    haso = True
                if new[y][x] == "x":
                    hasx = True
        else:
            if haso:
                parr[j][i] = "O"
            if hasx:
                parr[j][i] = old
            if not haso and not hasx:
                parr[j][i] = "I"

print(sum([1 for y1 in parr for x1 in y1 if x1 == "I"]))


# for i in range(len(parr)):
#     parr[i] = ''.join(parr[i]) + "\n"
# with open("out.txt", "w") as f:
#     for i in parr:
#         f.write(i)



for i in range(len(new)):
    new[i] = ''.join(new[i]) + "\n"
with open("out.txt", "w") as f:
    for i in new:
        f.write(i)