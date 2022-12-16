# rope model

def touching(p1: "tuple[int,int]", p2: "tuple[int,int]"):
    delta_x = p2[0] - p1[0]
    delta_y = p2[1] - p1[1]
    return (abs(delta_x) in [0,1]) and (abs(delta_y) in [0,1])

def update_head(h: "tuple[int,int]", h_move):
    return (h[0] + h_move[0], h[1] + h_move[1])

def update_tail(t: "tuple[int,int]", h: "tuple[int,int]"):
    if touching(t, h):
        return t
    
    normalize = lambda x: x//abs(x) if x != 0 else 0
    
    delta_x = h[0] - t[0]
    delta_y = h[1] - t[1]
        
    new_t = (t[0] + normalize(delta_x), t[1] + normalize(delta_y))
    
    return new_t
    
def parse_moves(txt):
    moves = []
    move_list = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    with open(txt) as f:
        for line in f:
            move, reps = line.rstrip().split()
            reps = int(reps)
            move = move_list[move]
            for _ in range(reps):
                yield move

def part1(txt):
    h = (0,0)
    t = (0,0)
    move = parse_moves(txt)
    seen = []
    while True:
        try:
            m = next(move)
            h = update_head(h, m)
            t = update_tail(t, h)
            seen.append(t)

        except StopIteration:  
              break
    
    return seen

print(len(set(part1('2022/day9.txt'))))

def part2(txt):
    h = (0,0)
    t = [(0,0)] * 9
    
    move = parse_moves(txt)
    seen = []
    while True:
        try:
            m = next(move)
            h = update_head(h, m)
            t[0] = update_tail(t[0], h)
            for i in range(len(t)-1):
                t[i+1] = update_tail(t[i+1], t[i])
            seen.append(t[-1])

        except StopIteration:  
              break
    
    return seen

def visualize(coords_list):
    coords = list(set(coords_list))
    x_min, x_max = [coords[0][0],coords[0][0]]
    y_min, y_max = [coords[0][1],coords[0][1]]
    for (x,y) in coords:
        if x > x_max:
            x_max = x
        if x < x_min:
            x_min = x
        if y > y_max:
            y_max = y
        if y < y_min:
            y_min = y
    x_range = x_max - x_min
    y_range = y_max - y_min
    
    grid = [['.' for _ in range(x_range+1)] for _ in range(y_range+1)]
    print(grid)
    for x, y in coords:
        # print(f'{x,y=}')
        grid[y - y_min][x - x_min] = '#'
        
    grid[-y_min][-x_min] = 'S'
    
    for i in range(len(grid)):
        print(''.join(grid[i]))
    print(len(grid))
    print(f'{x_min,x_max=}')
    print(f'{y_min,y_max=}')
seen = part2('2022/day9.txt')
print(len(set(seen)))
visualize(seen)