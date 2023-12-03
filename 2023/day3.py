with open("day3.txt") as f:
    txt = [x.strip() for x in f.read().split()]


def adj(i,j, maxi, maxj):
    pm = [-1,0,1]
    out = []
    for x in pm:
        for y in pm:
            if i + x > maxi or i + x < 0 or j + y > maxj or j + y < 0: continue
            out.append((i+x,j+y))
    return out

def search(i, arr):  
    if arr[i] not in "1234567890": 
        return 0, (i, i)  
    right = arr[i:]
    left = arr[:i] if i==0 or arr[i-1] in '1234567890' else ""
    for c in right:
        if c not in '1234567890':
            right = right.replace(c, " ")
    for c in left:
        if c not in '1234567890':
            left = left.replace(c, " ")
    right = right.split()[0]
    left = "" if len(left.split()) == 0 else left.split()[-1]
    return (int(left+right), (i-len(left), i+len(right)-1))

s1 = 0
s2 = 0
seen = []
ast_seen = []
for i in range(len(txt[0])):
    for j in range(len(txt)):
        if txt[j][i] not in '.1234567890':
            gears = []
            for adji, adjj in adj(i,j, len(txt[0]), len(txt)):
                if (adji, adjj) in seen:
                    if txt[adjj][adji] == "*" and (adji, adjj) not in ast_seen:  ## This block wasn't necessary for my input
                        num, loc = search(adji, txt[adji])                       ## but I wrote it anyway. Just in case a number
                        gears.append(num)                                        ## has been seen by a previous operator before
                        for m in range(loc[0],loc[1]+1):                         ## the gear it's part of. 
                            ast_seen.append((m, adjj))
                    continue
                if txt[adjj][adji] in '1234567890':                    
                    num, loc = search(adji, txt[adjj])
                    if txt[j][i] == "*":
                        gears.append(num)
                    s1 += num
                    for m in range(loc[0],loc[1]+1):
                        seen.append((m, adjj))
            if len(gears) == 2:
                s2 += gears[0] * gears[1]

# filled = [[" " for _ in range(len(txt[0]))] for _ in range(len(txt))]
# for x,y in seen:
#     filled[y][x] = "X"

# print('\n'.join(txt))
# print('\n'.join([''.join(line) for line in filled]))
print(s1)
print(s2)