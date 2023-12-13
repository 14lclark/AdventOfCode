a = "day14.txt"
b = "day14test.txt"
with open(a) as f:
    txt = [list(x) for x in f.read().strip().split("\n")]

# print(txt)

def move_left(x):
    for j in range(len(x)):
        for i in range(len(x[0])):
            if x[j][i] != "O":
                continue
            for l in range(i, -1, -1):
                if l == 0 or (x[j][l-1] == "O" or x[j][l-1] == "#"):
                    x[j][i] = '.'
                    x[j][l] = 'O'
                    break
    return x

transpose = lambda x: list(map(list, zip(*x))) 

# part 1
copy = transpose(txt)
for i in range(1):
    copy = move_left(copy)
copy = transpose(copy)

s = 0
for j in range(len(copy)): 
    for i in range(len(copy[0])):
        if copy[::-1][j][i] == "O":
            s += j+1

print(s)

rt = lambda x: transpose(x[::-1])
tr = lambda x: transpose(x)[::-1]
def solve(x):
    #North
    x = transpose(x)
    x = move_left(x)
    x = transpose(x)

    #West
    x = move_left(x)

    #South
    x = rt(x)
    x = move_left(x)
    x = tr(x)

    #East
    x = rt(rt(x))
    x = move_left(x)
    x = tr(tr(x))

    return x

def check_for_cycle(c):
    for i in range(len(c)):
        for j in range(i+1, len(c)):
            if c[i:j+1] == c[j+1:j+1+j-i+1]:
                return i, j-i+1
    return -1, -1

cache = []
for i in range(1000000000):
    txt = solve(txt)
    cache.append(txt)
    ind, length = check_for_cycle(cache)
    if ind >= 0:
        break


    
cycle = length
# print(cycle)
cache_num = (1000000000-ind-1) % cycle
txt = cache[ind:ind+length+1][cache_num]

s = 0
for j in range(len(txt)): 
    for i in range(len(txt[0])):
        if txt[::-1][j][i] == "O":
            s += j+1

print(s)