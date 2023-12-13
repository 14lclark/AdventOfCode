with open("day12.txt") as f:
    # txt = [(list(x.split(" ")[0]), eval("[" + x.split(" ")[1] + "]")) for x in f.read().strip().split("\n")]
    txt = [(x.split(" ")[0], eval("[" + x.split(" ")[1] + "]")) for x in f.read().strip().split("\n")]
# 

from itertools import product, permutations


# Original solution to part 1
# def search(rec, groups):
#     # print(rec)
#     rec = list(rec)
#     inds = []
#     for i in range(len(rec)):
#         if rec[i] == "?":
#             inds.append(i)    

#     count = 0
#     for perm in product('.#', repeat=len(inds)):
#         copy = rec.copy()
#         for i, ind in enumerate(inds):
#             copy[ind] = perm[i]
#         rec_groups = ''.join(copy).split('.')
#         while '' in rec_groups:
#             rec_groups.remove('')
#         if [len(x) for x in rec_groups] == groups:
#             count += 1
#     return count

# s = 0
# for record, groups in txt:
#     s += search(record, groups)
# print(s)




# part 2

from functools import cache

@cache
def recursive(rec, groups, orig_len=0):
    # indent = "    " * (orig_len - len(groups))
    # print(indent + "record: ", rec)
    if len(groups) == 0 and "#" in rec:
        # print(indent + "no groups left, but still have #")
        return 0
    elif len(groups) == 0:
        return 1
    if rec == "":
        # print("unassigned groups, not enough to assign: empty record")
        return 0
    if sum(1 for x in rec if x in '?#') < groups[0] or len(rec) < groups[0]:
        # print("unassigned groups, not enough to assign: not enough # and ?")
        return 0
    group = groups[0]
    poss = []
    for j in range(len(rec)):
        if  j + group <= len(rec) and all(x in '?#' for x in rec[j:j+group]) and ('?' in rec[j:j+group] or rec[j:j+group] == "#"*group) and (j+group == len(rec) or rec[j+group] in '.?'):
            if (j == 0 or rec[j-1] != "#") and "#" not in rec[:j]:
                poss.append(j+group+1)

    count = [1 for _ in range(len(poss))]
    # print()
    # print(indent + "group: ", groups[0])
    # print()
    for i in range(len(poss)):
        j = poss[i] - group - 1
        # print(indent + "possibility: ",j, rec[j:j+group])
        # print(indent + "-------------")
        count[i] *= recursive(rec[poss[i]:], groups[1:], orig_len)
        # print()
    # print("GROUP AND COUNT ", group, count)
    # print(indent + "Count: ", sum(count))
    return sum(count)

txt2 = [(x + "?" + x + "?" + x + "?" + x + "?" + x, y*5) for x,y in txt]

s = 0
for record, groups in txt:
    s += recursive(record, tuple(groups))
print(s)

s = 0
for record, groups in txt2:
    s += recursive(record, tuple(groups))

print(s)