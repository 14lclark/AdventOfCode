a = 'day15.txt'
b = 'day15test.txt'
with open(a) as f:
    txt = [x for x in f.read().strip().split(',')]

def hash(x):
    curr = 0
    for c in x:
        curr += ord(c)
        curr *= 17
        curr = curr % 256
    return curr
s = 0
for x in txt:
    s += hash(x)
print(s)

#part 2
txt = [(x.split("=")[0], int(x.split("=")[1])) if '=' in x else [x.split('-')[0]] for x in txt]
boxes = [list() for _ in range(256)] 
for x in txt:
    i = hash(x[0])
    if len(x) == 2:
        for j, y in enumerate(boxes[i]):
            if y[0] == x[0]:
                boxes[i][j] = x
                break
        else:
            boxes[i].append(x)
    elif len(x) == 1:
        for j, y in enumerate(boxes[i]):
            if y[0] == x[0]:
                ind = j
                break
        else:
            continue
        boxes[i].pop(j)

def f_power(box, i):
    p = 0
    for j, lens in enumerate(box):
        p += (i+1) * (j+1) * lens[1]
    return p

p = 0
for i, box in enumerate(boxes): 
    p += f_power(box, i)
print(p)
