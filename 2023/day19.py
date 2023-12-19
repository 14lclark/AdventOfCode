a = 'day19.txt'
# a = 'day19test.txt'

with open(a) as f:
    methods = {}
    curr = f.readline().strip()
    while curr != "":
        parsed = []
        parsed = curr.split("{")
        methods[parsed[0]] = parsed[1][:-1].split(",")
        curr = f.readline().strip()
    parts = [[tuple(x.split("=")) for x in line.strip()[1:-1].split(",")] for line in f.read().strip().split('\n')]
    parts = list(map(dict, parts))

def follow(p, method):
    if method == "A" or method == "R":
        print(method)
        return method
    print(p, method)
    for ins in methods[method]:
        print(ins)
        if ":" in ins:
            cond, res = ins.split(":")
            cond = cond.replace(cond[0], str(p[cond[0]]))
            print(cond)
            if eval(cond):
                return follow(p, res)
        elif ":" not in ins:

            return follow(p, ins)

accept = []
reject = []
for part in parts:
    ar = follow(part, 'in')
    if ar == 'R':
        reject.append(part)
    else:
        accept.append(part)
s=0
for i in accept:
    for j in i:
        s+=int(i[j])
print(s)

# part 2

def overlap(x, y):
    xstart = x[0]
    xend = x[1]
    ystart = y[0]
    yend = y[1]
    if (xstart <= xend < ystart) or (xend >= xstart > yend):
        i = None
        o = [x]
    elif xstart <= ystart:
        if xstart < ystart:
            o = [(xstart, ystart-1)]
        else: 
            o = []
        if xend <= yend:
            i = (ystart, xend)    
        elif xend > yend:
            i = (ystart, yend)
            o.append((yend+1, xend))
    elif ystart<=xstart:
        if xend <= yend:
            i = x
            o = []
        else:
            i = (xstart, yend)
            o = [(yend+1, xend)]
    return {'in': i, 'out': o}


start = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}

def follow2(p: dict, method: str):
    if method == "A":
        return [p]
    if method == "R":
        return []
    acc = []
    for ins in methods[method]:
        if ":" in ins:
            cond, res = ins.split(":")
            if cond[1] == "<":
                interval = (1,int(cond.split("<")[1])-1)
            else:
                interval = (int(cond.split(">")[1])+1, 4000)
            pcopy = p.copy()
            ov = overlap(p[cond[0]], interval)
            pcopy[cond[0]] = ov['in']
            p[cond[0]] = ov['out'][0]
            acc += follow2(pcopy, res)
        elif ":" not in ins:
            acc += follow2(p, ins)
    return acc

outvals = follow2(start, 'in')

s = 0
for val in outvals:
    mid = 1
    for key in val:
        mid *= val[key][1] - val[key][0] + 1
    s += mid

print(s)
