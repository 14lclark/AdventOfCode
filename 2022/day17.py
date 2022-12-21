# falling rocks
def visualize(coords, new_coords, max_height=None):
    if max_height is None:
        max_y = max([y for (_,y) in coords + new_coords])
    else:
        max_y = max_height
        
    out = [['.' for _ in range(7)] for _ in range(max_y)]
    
    for (x, y) in coords:
        out[y-1][x] = '#'
    
    for (x, y) in new_coords:
        out[y-1][x] = '@'
    out = out[::-1]
    for i in out:
        print(''.join(i))
        
def loop(iterable):
    i = 0
    length = len(iterable)
    while True:
         yield iterable[i]
         i = (i+1) % length

def parse_moves(txt):
    with open(txt) as f:
        moves = f.readline().rstrip()
    return moves

pieces = [[(i, 1) for i in range(2,6)],               # --
          [(2,2), (3,2), (4,2), (3,3), (3,1)],        # +
          [(i, 1) for i in [2,3,4]] + [(4,2), (4,3)], # _|
          [(2, i) for i in range(1,5)],               # |
          [(2,1), (2,2), (3,1), (3,2)]]               # square
   
def update_until_settled(move_iterator, grid, new_rock_index):
    rocks = grid['coords']
    max_height = grid['height']
    
    def allowed_position(new_pos):
        seen = [False for i in range(7)]
        for i in range(len(rocks)-1, 0, -1):
            seen[rocks[i][0]] = True 
            if all(seen):
                all_coords_seen_index = i
                
                break
        else:
            all_coords_seen_index=0
        for i in new_pos:
            x, y = i
            if i in rocks[all_coords_seen_index:] or x < 0 or x > 6 or y == 0:
                return False
        return True
            
    def jets(falling_rock, move):
        if move == '<':
            shift = -1
        elif move == '>': 
            shift = 1
        new_rock_pos = [(x + shift, y) for (x,y) in falling_rock]
        if allowed_position(new_rock_pos):
            return new_rock_pos
        return falling_rock
    
    def gravity(falling_rock):
        new_rock_pos = [(x, y - 1) for (x,y) in falling_rock]
        if allowed_position(new_rock_pos):
            return new_rock_pos
        return falling_rock
    
    def create_rock():
        new = [(x, y + max_height + 3) for (x,y) in pieces[new_rock_index]]
        return new
        
    new_rock = create_rock()
    # visualize(rocks, new_rock)    
    while True:
        
        # print()
        m = next(move_iterator)
        new_rock = jets(new_rock, m)
        old_rock = new_rock.copy()
        new_rock = gravity(new_rock)
        # visualize(rocks, new_rock)
        if new_rock == old_rock:
            break
    
    
    grid['coords'] += new_rock
    
    maxh = grid['height']
    for (_,y) in new_rock:
        if y > grid['height']:
            grid['height'] = y

    return grid


def part1(txt):
    # moves = parse_moves(txt)
    moves = '>'
    print(len(moves))
    moves = loop(moves)
    
    # grid : {max_height: [rock coords]}
    grid = {'height': 0, 'coords': []}
    heights = []
    for i in range(2022):
        rock_index = i % 5
        grid = update_until_settled(moves, grid, rock_index)
        heights.append(grid['height'])
    
    return grid, heights
# grid, heights = part1('2022/day17test.txt')
# print(grid['height'])
# diffs = [heights[i] - heights[i-1] for i in range(1,len(heights))]
# print(diffs)

# visualize(grid)

def part2(txt):
    moves = parse_moves(txt)
    print(len(moves))
    moves = loop(moves)
    
    # grid : {max_height: [rock coords]}
    grid = {'height': 0, 'coords': []}
    heights = []
    k = 0
    last_height = 0
    diffs = []
    while True:
        rock_index = k % 5
        grid = update_until_settled(moves, grid, rock_index)
        heights.append(grid['height'])
        if k == 10_000:
            break
    
    for i in range(10_001//2):    
        print(i)
        found = not any(heights[j+i] - heights[j] != 0 for j in range(10_001//2))
        if found:
            print(i)
        if i % 1000 == 0:
            print(i)
    return grid, i//2

grid, cycle_length = part2('2022/day17test.txt')
# print(cycle_length)