
with open("day11.txt") as f:
    txt = [[y for y in x] for x in f.read().strip().split("\n")]

empty_rows = []

for j in range(len(txt)):
    if "#" not in txt[j]:
        empty_rows.append(j)

transpose = lambda x: [list(i) for i in zip(*x)]
empty_cols = []

transposed = transpose(txt)
for i in range(len(txt[0])):
    if "#" not in transposed[i]:
        empty_cols.append(i)

# Original with two arrays (for posterity)
# gals1 = []
# gals2 = []
# for j in range(len(txt)):
#     for i in range(len(txt[0])):
#         if txt[j][i] == "#":
#             x_shift = 0
#             y_shift = 0
#             for x in empty_cols:
#                 if x < i:
#                     x_shift += 1
#             for y in empty_rows:
#                 if y < j:
#                     y_shift += 1
#             gals1.append((i + x_shift, j + y_shift))
#             gals2.append((i + x_shift * 999999, j + y_shift * 999999))


# Refactor into a function; all coefficients in array so we don't 
# have to re-loop through the entire universe for each one
def expand(uni, exp_coeffs=[2,1000000]):
    gals = {c: [] for c in exp_coeffs}
    for j in range(len(txt)):
        for i in range(len(txt[0])):
            if txt[j][i] == "#":
                x_shift = 0
                y_shift = 0
                for x in empty_cols:
                    if x < i:
                        x_shift += 1
                for y in empty_rows:
                    if y < j:
                        y_shift += 1
                for c in exp_coeffs:
                    gals[c].append(
                        (i + x_shift * (c - 1), j + y_shift * (c - 1))
                        )
                
    return gals

gals = expand(txt)

# total = 0
# for ind1 in range(len(gals[2])):
#     gal1 = gals[2][ind1]
#     for ind2 in range(ind1+1, len(gals[2])):
#         gal2 = gals[2][ind2]
#         dist =  abs(gal1[0] - gal2[0]) + abs(gal1[1] - gal2[1])

#         # print(ind1, ind2, dist)
#         total += dist
# print(total)

# total = 0
# for ind1 in range(len(gals[10**6])):
#     gal1 = gals[10**6][ind1]
#     for ind2 in range(ind1+1, len(gals[10**6])):
#         gal2 = gals[10**6][ind2]
#         dist =  abs(gal1[0] - gal2[0]) + abs(gal1[1] - gal2[1])
#         # print(ind1, ind2, dist)
#         total += dist
# print(total)


# "Refactoring" both parts into one less easy to understand loop.
# Really just should have used numpy to get be able to broadcast 
# over arrays instead of this nightmare of list comprehensions

total = [0 for x in gals]
galsvals = list(gals.values())
for ind1 in range(len(gals[2])):
    gal1 = [g[ind1] for g in galsvals]
    for ind2 in range(ind1+1, len(galsvals[0])):
        gal2 = [g[ind2] for g in galsvals]
        dist =  [abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) for g1,g2 in zip(gal1, gal2)]
        total = [t + d for t,d in zip(total, dist)]
print(total)