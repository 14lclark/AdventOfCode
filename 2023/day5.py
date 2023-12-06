with open("day5.txt") as f:
    seeds = f.readline()[7:].strip().split(" ")
    txt = [x.strip() for x in f.read().strip().split("\n") if x != '']

splits = [x for x in range(len(txt)) if txt[x] != '' and txt[x][0] not in '1234567890']
maps = []
for x in range(len(splits)-1):
    maps.append(txt[splits[x]+1:splits[x+1]])
maps.append(txt[splits[-1]+1:])
maplist = []

for i in range(len(maps)):
    maplist.append([])
    for map in maps[i]:
        info = [int(m) for m in map.split(" ")]
        s = range(info[1], info[1] + info[2])
        d = info[0]
        maplist[i].append({'s': s,'dstart': d})

closest = None
for seed in seeds:
    copy = int(seed)
    for map in maplist:
        for ranges in map:
            if copy in ranges['s']:
                copy = copy - ranges['s'][0] + ranges['dstart']
                break
    if closest is None or copy < closest:
        closest = copy
print(closest)

#part 2

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

shift = lambda x, i: (x[0] + i, x[1] + i)

seedstarts = [int(seeds[i]) for i in range(0, len(seeds), 2)]
seedranges = [int(seeds[i]) for i in range(1, len(seeds), 2)]

vals =  [
            [
             [(seedstarts[i], seedstarts[i] + seedranges[i])]
               for i in range(len(seedstarts))
            ]
        ]
index = 1

for map in maplist:
    vals.append([])
    seen = []
    for current in vals[index-1]:
        current = current[:]
        appends = []
        while len(current) != 0:
            appends = []
            one = False
            for range in map:
                intv = (range['s'][0], range['s'][-1])
                over = overlap(current[-1], intv)
                if over['in'] is not None:
                    one = True
                    sh = [shift(over['in'], range['dstart'] - intv[0])]
                    if sh not in vals[index]:
                        vals[index].append(sh)               

                for out in over['out']:
                    if out not in current:
                        appends.append(out)
            if not one:
                vals[index].append([current[-1]])
            current.pop()
            current += appends
            
        vals[index] += current
    index += 1

closest = None
for i in vals[-1]:
    if closest is None or i[0] < closest:
        closest = i[0] 
print(closest)