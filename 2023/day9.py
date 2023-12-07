with open("day9.txt") as f:
    txt = [[int(y) for y in x.strip().split(" ")] 
           for x in f.read().strip().split("\n")]

def diffs(x):
    new = []
    prev = x[0]
    for i in x[1:]:
        new.append(i - prev)
        prev = i
    return new

out1 = []
out2 = []
for x in txt:
    lasts = [x[-1]]
    firsts = [x[0]]
    next = diffs(x)
    while next != [0]*len(next):
        lasts.append(next[-1])
        firsts.append(next[0])
        next = diffs(next)
    lasts.append(0)
    firsts.append(0)
    l = 0
    p = 0
    for i in reversed(range(1,len(lasts))):
        l = lasts[i-1] + l
        p = firsts[i-1] - p
    out1.append(l)
    out2.append(p)
print(sum(out1))
print(sum(out2))
        
    
