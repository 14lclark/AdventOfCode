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
                    
def part2():
    pass
