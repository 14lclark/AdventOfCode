with open("day6test.txt") as f:
    [x for x in f.read().strip().split("\n")]
timedist = [(62,644),(73,1023),(75,1240),(65,1023)]

l = []
for td in timedist:
    count = 0
    for i in range(td[0]):
        if i * (td[0]-i) > td[1]:
            count += 1
    l.append(count)
prod = 1
for elt in l:
    prod *= elt

print(prod)

count = 0
for i in range(62737565):
    if i * (62737565-i) > 644102312401023:
        count += 1
print(count)