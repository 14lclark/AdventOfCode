# section cleaning



def part1():
    
    def sub(p1,p2):
        return [p1[0]-p2[0], p1[1]-p2[1]]
                
    total = 0
    with open('2022/day4.txt') as f:
        
        for line in f:
            sections = [[int(j) for j in i.split("-")] for i in line.rstrip().split(",")]
            diff = sub(sections[0],sections[1])
            if diff[0] * diff[1] <= 0:
                total += 1
    print(total)

def part2():
    
    def antisub(p1,p2):
        return [p1[0]-p2[1], p1[1]-p2[0]]
    
    total = 0
    with open('2022/day4.txt') as f:
        
        for line in f:
            sections = [[int(j) for j in i.split("-")] for i in line.rstrip().split(",")]
            diff = antisub(sections[0],sections[1])
            if diff[0] * diff[1] <= 0:
                total += 1
    print(total)

part2()