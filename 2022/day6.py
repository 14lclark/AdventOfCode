def search_for_consecutive_unique(s, num):
    for i in range(num-1, len(s)):
            for j in range(i-num+1, i+1):
                temp = s[i-num+1:i+1]
                temp.remove(s[j])
                if s[j] in temp:
                    break
            else:
                print(s[i-num+1:i+1])
                return i

def part1():
    with open('2022/day6.txt') as f:
        buffer = f.readline()
        buffer = [*buffer]
        # zero indexing so add 1
        return search_for_consecutive_unique(buffer,4) + 1

# print(part1())

def part2():
    with open('2022/day6.txt') as f:
        buffer = f.readline()
        buffer = [*buffer]
        # zero indexing so add 1
        return search_for_consecutive_unique(buffer,14) + 1
    
print(part2())    
