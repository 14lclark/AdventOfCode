def crawl(dir):
    pass

def part1():
    #full directory structure
    top = {}

    #append on cd x
    #pop on cd ..
    current_path = []

    with open('2022/day7.txt') as f:
        for line in f:
            cmd = line.split()
            if cmd[0] == '$':
                if cmd[1] == 'cd':
                    if cmd[2] == '/':
                        current_path = []
                        
                    elif cmd[2] == '..':
                        current_path.pop()
                        
                    else:
                        current_path.append(cmd[2])
                        if cmd[2] == '/': 
                            print('oh no')

                    continue

                if cmd[1] == 'ls':
                    continue

            current_path_str = '/'
            for i in current_path:
                current_path_str += i +'/'
            try:
                top[current_path_str]
            except KeyError:  
                top[current_path_str] = []

            if cmd[0] == 'dir':
                top[current_path_str] += [{cmd[1]: current_path+[cmd[1]]}]
                continue

            if isinstance(cmd[0], int):
                    top[current_path_str] += [cmd]

            top[current_path_str] += cmd
    print(top)
            
part1()