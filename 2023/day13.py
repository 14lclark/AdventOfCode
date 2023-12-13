with open("day13.txt") as f:
    txt = [[]]
    i = 0
    for line in f:
        if line.strip() == "":
            txt.append(list())
            i += 1
        else:
            txt[i].append(list(line.strip()))

def transpose(x):
    return list(map(list, zip(*x)))

#Part 1 original

# def check(x):
#     for i in range(len(x)-1):
#         if x[i] == x[i+1]:
#             for j in range(1,
#                            min(len(x) - (i + 1), i+1)
#                         ):
#                 if x[i-j] != x[i+j+1]:
#                     break
#             else:
#                 return i
#     return -1
# s = 0
# for x in txt:
#     i = check(x) 
#     if i >= 0:
#         s += 100 * (i+1)
#         continue
#     i = check(transpose(x))
#     if i >= 0:
#         s += i+1
    

# print(s)

#Part 2 original

# def check2(x):
#     for i in range(len(x)-1):
#         diffs = 0
#         for j in range( min(len(x)-(i+1), i+1) ):
#             for elt in [a == b for a,b in zip(x[i-j], x[i+j+1])]:
#                 if not elt:
#                     diffs += 1
#         if diffs == 1:
#             return i
#     return -1

# s = 0
# for x in txt:
#     i = check2(x) 
#     if i >= 0:
#         s += 100 * (i+1)
#         continue
#     i = check2(transpose(x))
#     if i >= 0:
#         s += i+1

# print(s)

# Refactored version
def check(x, num_diffs_allowed):
    for i in range(len(x)-1):
        diffs = 0
        for j in range( min(len(x)-(i+1), i+1) ):
            for a,b in zip(x[i-j], x[i+j+1]):
                if a != b:
                    diffs += 1
        if diffs == num_diffs_allowed:
            return i
    return -1
for k in [0,1]:
    s = 0
    for x in txt:
        i = check(x,num_diffs_allowed=k) 
        if i >= 0:
            s += 100 * (i+1)
            continue
        i = check(transpose(x),num_diffs_allowed=k)
        if i >= 0:
            s += i+1
    print(s)