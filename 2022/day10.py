# CPU instructions
from functools import lru_cache

def parse(txt):
    instructions = [] 
    with open(txt) as f: 
        for line in f: 
            line = line.rstrip()
            if line == 'noop': 
                instructions.append('noop')
            else: 
                cmd, amt = line.split()
                amt = int(amt)
                instructions.append(cmd)
                instructions.append(amt)
    return instructions

def evaluate(instructions, cycle_num):
    return 1 + sum([i for i in instructions[:cycle_num-1] if isinstance(i,int)])

def part1(txt, important_cycles):
    instructions = parse(txt)
    reg_signal = 1
    next_add = 0
    signal_strength = 0
    for i in important_cycles:
        signal_strength += evaluate(instructions, i) * i

    return signal_strength


def part2(txt, lines, px_per_line):
    instructions = parse(txt)
    middle_coord = [evaluate(instructions, cycle) for cycle in range(1, lines * px_per_line + 1)]
    crt = [['.' for _ in range(px_per_line)] for _ in range(lines)]
    
    for cycle in range(0, lines * px_per_line):
        if (cycle) % 40 in [middle_coord[cycle] + i for i in (-1, 0, 1)]:
             crt[(cycle) // 40][(cycle) % 40] = "#"
             
    return crt
print(part1('2022/day10.txt', [20,60,100,140,180,220]))

screen =  part2('2022/day10.txt', 6, 40)
[print(''.join(i)) for i in screen]
            