
def transpose(rect):
    #non jagged transpose
    return [[row[i] for row in rect] for i in range(len(rect[0]))]

def move_stack(stacks, moves, how_many_at_once=1):
    final = stacks
    num = moves[0]
    origin = moves[1] - 1
    dest = moves[2] - 1
    temp = []
    for _ in range(num // how_many_at_once):
        for _ in range(how_many_at_once):
            temp.append(final[origin].pop())
        for _ in range(how_many_at_once):
            final[dest].append(temp.pop())
    return final

def part(number):
    with open('2022/day5.txt') as f:
        line = f.readline()
        
        stacks = []
        while " 1" not in line:
            stacks.append([*line.rstrip()])
            line = f.readline()
        
        stacks = transpose(stacks[::-1])
        stacks = [i for i in stacks if ('[' not in i) and (']' not in i)]
        stacks = [stacks[i] for i in range(len(stacks)) if i%2==0]
        for i in stacks:
            while i[-1] == ' ':
                i.pop()
    
        f.readline()
        for line in f:
            moves = [int(i) for i in line.rstrip().split() if 'o' not in i]
            if number == 1:
                stacks = move_stack(stacks, moves, 1)
            if number == 2:
                stacks = move_stack(stacks, moves, moves[0])
        
        for i in stacks:
            print(i.pop(), end="")
            
        print()
            
        


part(2)