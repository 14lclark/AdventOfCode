# visible trees

def get_column(grid, col_num):
    return [grid[i][col_num] for i in range(len(grid))]

def print_return(x):
    print(x)
    return x

def is_visible(grid, row_num, col_num) -> bool:
    # doesn't work, not sure why
    
    #row index is which row you are in
    #column index is which column you're in
    #  XXXXX
    #  XXXAX
    #  XXXXX
    #  XXXXX
    # so the A above has row_num=2 and col_num=4
    #relies on non jagged lists
    col = get_column(grid, col_num)
    row = grid[row_num]
    if row_num == 0 or col_num == 0 \
       or row_num == (len(col)-1) or col_num == (len(row)-1):
        return True

    number_of_rows = len(grid)
    number_of_columns = len(row)
     
    value = row[col_num]
    blocked_left = (i > value for i in row[:col_num])
    # if not any(blocked_left):
    #     return True
    blocked_right = (i > value for i in row[-1:col_num:-1])
    # if not any(blocked_right):
    #     return True
    blocked_top = (i > value for i in col[:row_num])
    # if not any(blocked_top):
    #     return True
    blocked_bottom = (i > value for i in col[-1:row_num:-1])
    # if not any(blocked_bottom):
    #     return True

    # return False
    blocked = any(any(i) for i in zip(blocked_left, blocked_right, blocked_top, blocked_bottom))

    return not blocked
    

def get_grid(txt: str) -> "list[list[int]]":
    grid = []
    with open(txt) as f:
        for line in f:
            grid.append([*(line.rstrip())])
    return [[int(i) for i in row] for row in grid]



def part1(txt):
    grid = get_grid(txt)
    visible_num = len(visible_list(grid))
    
    return(visible_num)

def left_visible(grid):
    visible = []
    width = len(grid[0])
    height = len(grid)
    for row in range(height):
        highest = -1
        for col in range(width):
            if grid[row][col] > highest:
                visible.append((row,col))
                highest = grid[row][col]
    return visible

def right_visible(grid):
    visible = []
    width = len(grid[0])
    height = len(grid)
    for row in range(height):
        highest = -1
        for col in range(width - 1, -1, -1):
            if grid[row][col] > highest:
                visible.append((row,col))
                highest = grid[row][col]
    return visible

def top_visible(grid):
    visible = []
    width = len(grid[0])
    height = len(grid)
    for col in range(width):
        highest = -1
        for row in range(height):
            if grid[row][col] > highest:
                visible.append((row,col))
                highest = grid[row][col]
    return visible

def bottom_visible(grid: "list[list[int]]") -> list:
    visible = []
    width = len(grid[0])
    height = len(grid)
    for col in range(width):
        highest = -1
        for row in range(height - 1, -1, -1):
            if grid[row][col] > highest:
                visible.append((row,col))
                highest = grid[row][col]
    return visible

def visible_list(grid):
    return (((set(left_visible(grid)) \
             | set(right_visible(grid))) \
             | set(top_visible(grid))) \
             | set(bottom_visible(grid)))
    
def scenic_scores(grid: "list[list[int]]", row_num, col_num):
    col = get_column(grid, col_num)
    row = grid[row_num]
    if row_num == 0 or col_num == 0 \
       or row_num == (len(col)-1) or col_num == (len(row)-1):
        return 0
    found_left = False
    found_right = False
    found_up = False
    found_down = False
    distance = 0
    score = 1
    self_height = grid[row_num][col_num]
    
    while True:
        distance += 1

        if not found_left and \
            (col_num - distance == 0 or self_height <= row[col_num-distance]):
                found_left = True
                score *= distance
        if not found_right and \
            (col_num + distance == len(row) - 1 or self_height <= row[col_num+distance]):
                found_right = True
                score *= distance

        if not found_up and \
            (row_num - distance == 0 or self_height <= col[row_num-distance]):
                found_up = True
                score *= distance

        if not found_down and \
            (row_num + distance == len(col) - 1 or self_height <= col[row_num+distance]):
                found_down = True
                score *= distance

        if found_down and found_left and found_right and found_up:
            break
    
    return score
        
def part2(txt):
    grid = get_grid(txt)
    grid_height = len(grid)
    grid_width = len(grid[0])
    scenic_score_max = 0
    for row_num in range(grid_height):
        for col_num in range(grid_width):
            scenic_score = scenic_scores(grid, row_num, col_num)
            if  scenic_score > scenic_score_max:
                scenic_score_max = scenic_score
    
    return scenic_score_max
    
    
    
# print(part1('2022/day8.txt'))
print(part2('2022/day8.txt'))
