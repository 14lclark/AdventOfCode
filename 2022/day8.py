# visible trees

def get_column(grid, col_num):
    return [grid[i][col_num] for i in range(len(grid))]

def printurn(x):
    print(x)
    return x

def is_visible(grid, row_num, col_num) -> bool:
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
    

def get_grid(txt: str) -> list[list[int]]:
    grid = []
    with open(txt) as f:
        for line in f:
            grid.append([*(line.rstrip())])

    print(grid[0])
    return [[int(i) for i in row] for row in grid]



def part1(txt):
    grid = get_grid(txt)
    visible_num = len(printurn(visible_list(grid)))
    
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
    # print(visible)    
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
    # print(visible)
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
    # print(visible)
    return visible

def bottom_visible(grid: list[list[int]]) -> list:
    visible = []
    width = len(grid[0])
    height = len(grid)
    for col in range(width):
        highest = -1
        for row in range(height - 1, -1, -1):
            if grid[row][col] > highest:
                visible.append((row,col))
                highest = grid[row][col]
    # print(visible)
    return visible

def visible_list(grid):
    return (((set(left_visible(grid)) \
             | set(right_visible(grid))) \
             | set(top_visible(grid))) \
             | set(bottom_visible(grid)))
            

print(part1('2022/day8.txt'))
