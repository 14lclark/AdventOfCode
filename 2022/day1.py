# snack calories

def part1():
    large = 0
    with open('./2022/day1.txt') as f:
        acc = 0
        for line in f:

            if line == "\n":
                if acc > large:
                    large = acc
                acc = 0
                continue

            acc += int(line)

        if acc > large:
            large = acc

    print(large)

def part2():
    large = []
    with open('./2022/day1.txt') as f:
        acc = 0
        for line in f:

            if line == "\n":
                large.append(acc)
                acc = 0
                continue

            acc += int(line)

        large.append(acc)
        large.sort(reverse=True)

    print(large[0]+large[1]+large[2])
part1()
part2()