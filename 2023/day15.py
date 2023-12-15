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

txt = [(x.split("=")[0], int(x.split("=")[1])) if '=' in x else [x.split('-')[0]] for x in txt]
print(txt)

boxes = [list() for _ in range(256)] 

for x in txt:
    i = hash(x[0])
    if len(x) == 2:
        for j, y in enumerate(boxes[i]):
            if y[0] == x[0]:
                boxes[i][j] = x
                break
        else:
            boxes[i] = [x] + boxes[i]
    elif len(x) == 1:
        ind = -1
        for j, y in enumerate(boxes[i]):
            if y[0] == x[0]:
                ind = j
                break
        else:
            continue
        boxes[i] = boxes[i][:j] + boxes[i][j+1:]

def f_power(box, i):
    p = 0
    for j, lens in enumerate(box):
        # print(lens, box)
        p += (i+1) * (j+1) * lens[1]
    return p

print(boxes)
p = 0
for i, box in enumerate(boxes):
    temp = f_power(box[::-1], i)
    # print(temp, box)
    p += temp

# print(p)
    
