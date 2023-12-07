with open("day8.txt") as f:
    dir = [(0 if x == 'L' else 1) for x in f.readline().strip()]
    paths = {x.split("=")[0].strip(): tuple(x.split("=")[1].strip()[1:-1].split(", ")) for x in f.read().strip().split("\n")}

curr = "AAA"
count = 0
while curr != "ZZZ":
    curr = paths[curr][dir[count % len(dir)]]
    count += 1
print(count)

#part 2

done = False
count = 0
curr_list = [x for x in paths if x[-1] == "A"]
first_z = [None for _ in curr_list]

while not done:
    for i in range(len(curr_list)):
        curr_list[i] = paths[curr_list[i]][dir[count % len(dir)]]
    count += 1
    for i in range(len(curr_list)):
        if curr_list[i][-1] == "Z" and first_z is not None:
            first_z[i] = count
    done = all([x is not None for x in first_z])

from math import lcm
print(lcm(*first_z))
