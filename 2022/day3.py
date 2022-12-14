# rucksack searching

letters = [chr(i) for i in range(97,97+26)] + [chr(i) for i in range(65,65+26)]
priorities = dict(zip(letters, range(1,53)))

def part1():
    total = 0
    with open('2022/day3.txt') as f:
        for line in f:
            line = line.rstrip()
            halves = [line[0:len(line)//2:1], line[len(line)//2:len(line):1]]
            for i in set(halves[0]):
                if i in set(halves[1]):
                    total += priorities[i]
        print(total)

def find_shared(s1: str, s2: str) -> str:
    shared = ""
    for i in s1:
        if i in s2 and i not in shared:
            shared += i
    return shared

def part2():
    total = 0
    with open('2022/day3.txt') as f:
        linenummod3 = 0
        lines = ["","",""]
        for line in f:
            lines[linenummod3] = line.rstrip()
            if linenummod3 == 2:
                total += priorities[find_shared(lines[0],find_shared(lines[1],lines[2]))]
            linenummod3 = int((linenummod3 + 1) % 3)
        
    print(total)

part2()