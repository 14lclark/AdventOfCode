a = "day16.txt"
b = "day16test.txt"

with open(a) as f:
    txt = [x for x in f.read().strip().split('\n')]

left = (-1, 0)
right = (1, 0)
up = (0, -1)
down = (0, 1)

pos = 1
dir = 2
rays = [{pos: (0,0), dir: right}]

def determine_energized(start, direction):
    energized = []
    rays = [{pos: start, dir: direction}]
    get = lambda x,y: x[y[1]][y[0]]
    add = lambda x,y: (x[0] + y[0], x[1] + y[1]) 
    refl = lambda x: (-1*x[0], -1*x[1]) 
    ccw = lambda x: (-1*x[1], x[0])
    cw = lambda x: ccw(ccw(ccw(x)))
    count = 0
    seen = []
    while len(rays) != 0:
        count += 1
        newrays = []
        rm = []
        for i, ray in enumerate(rays):
            x, y = ray[pos]
            dx, dy = ray[dir]
            # input()

            if not (0 <= x < len(txt[0])) or not (0 <= y < len(txt)):
                rm.append(ray)
                continue

            if ray[pos] not in energized:
                energized.append(ray[pos])
            if txt[y][x] == "|":
                if dy == 0:
                    rm.append(ray)
                    if ray not in seen:
                        seen.append(ray)
                        newrays.append({pos: ray[pos], dir: ccw(ray[dir])})
                        newrays.append({pos: ray[pos], dir: cw(ray[dir])})

            elif txt[y][x] == "-":
                if dx == 0:
                    rm.append(ray)
                    if ray not in seen:
                        seen.append(ray)
                        newrays.append({pos: ray[pos], dir: ccw(ray[dir])})
                        newrays.append({pos: ray[pos], dir: cw(ray[dir])})

            elif txt[y][x] == "/":
                if dy == 0:
                    rm.append(ray)
                    if ray not in seen:
                        seen.append(ray)
                        newrays.append({pos: ray[pos], dir: cw(ray[dir])})
                if dx == 0:
                    rm.append(ray)
                    if ray not in seen:
                        seen.append(ray)
                        newrays.append({pos: ray[pos], dir: ccw(ray[dir])})
            elif txt[y][x] == '\\':
                if dy == 0:
                    rm.append(ray)
                    if ray not in seen:
                        seen.append(ray)
                        newrays.append({pos: ray[pos], dir: ccw(ray[dir])})
                if dx == 0:
                    rm.append(ray)
                    if ray not in seen:
                        seen.append(ray)
                        newrays.append({pos: ray[pos], dir: cw(ray[dir])})

        for ray in rm:
            rays.remove(ray)
        for ray in newrays:
            rays.append(ray)
        for ray in rays:
            ray[pos] = add(ray[pos], ray[dir]) 
    return energized

m = 0
arg = None
for j in range(len(txt[0])):
    ed = determine_energized((j,0), down)
    eu = determine_energized((j, len(txt)-1), up)
    er = determine_energized((0, j), right)
    el = determine_energized((len(txt[0])-1, j), left)
    emax = max(map(len, [ed, eu, er, el]))
    if emax > m:
        m = emax

print(m)
# field = [["." for _ in range(len(txt[0]))] for _ in range(len(txt))]
# for i,j in arg[0]:
#     field[j][i] = "#"
# print()
# print('\n'.join([''.join(f) for f in field]))