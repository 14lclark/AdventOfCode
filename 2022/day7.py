def directory_size(dirs: dict, sumpath: str):
    total = 0
    for path, ls in dirs.items(): 
        if sumpath in path:
            for file, size in ls['files'].items():
                total += size

    return total
            
            
def make_file_structure(txt):
    #full directory structure
    top = {}
    
    #append on cd x
    #pop on cd ..
    current_path = []
    

    with open(txt) as f:
        for line in f:
            args = line.split()
            
            if args[0] == '$':
                if args[1] == 'cd':
                    if args[2] == '/':
                        current_path = []
                        
                    elif args[2] == '..':
                        current_path.pop()
                        
                    else:
                        current_path.append(args[2])
                            
                    current_path_str = '//'
                    for i in current_path:
                        current_path_str += i +'/'
                    try:
                        top[current_path_str]
                    except KeyError:  
                        top[current_path_str] = {'files': {}, 'dirs': {}}
                        
                    continue

                if args[1] == 'ls':
                    continue

            if args[0] == 'dir':
                top[current_path_str]['dirs'][args[1]] = current_path_str+args[1]
            else:
                top[current_path_str]['files'][args[1]] = int(args[0])
    return top

def part1(largest_size):
    top = make_file_structure('2022/day7.txt')
    
    total = 0
    for path in top:
        size = directory_size(top, path)  
        if size <= largest_size:
            # print(f"{size=}")
            total += size
            # print(f"{total=}")
    print(total)
            
# part1(100_000)

def part2(delete_size, file_system_size):
    top = make_file_structure('2022/day7.txt')
    
    smallest = file_system_size
    smallest_path = '/'
    
    count = 0
    for path in top:
        count += 1
        size = directory_size(top, path)
        print(size, path)
        if size >= delete_size and size <= smallest:
            smallest = size
            smallest_path = path
    # print(top)

    print(smallest_path, smallest)

# part2(1_000_000, 9_000_000_000)
    
# part2(8_381_165, 70_000_000)

###
# //rbmstsf/ngflwbmp/jthnmqs/zdvj/smjvcql/qcqljj/

def dir_str(dir):
    acc = ''
    for i in dir:
        acc += i + '/'
    return acc

def part2_second(txt):
    with open(txt) as f:
        current_dir = []
        
        # [dir, size]
        seen_and_size = []
        for line in f:
            args = line.split()
            if args[0] == '$':
                if args[1] == 'cd':
                    if args[2] == '/':
                        current_dir = ['top']
                        if current_dir not in [i[0] for i in seen_and_size]:
                            seen_and_size.append([current_dir, 0])
                            print('world')
                    elif args[2] == '..':
                        current_dir.pop()
                        
                    else:
                        # print(args[2])
                        current_dir.append(args[2])
                        print(f'{current_dir}')
                        print(f'{seen_and_size=}')
                        if current_dir not in [i[0] for i in seen_and_size]:
                            print(current_dir)
                            print('hello')
                            seen_and_size.append([current_dir, 0]) 
                            
                    continue
                if args[1] == 'ls':
                    continue
            if args[0] == 'dir':
                continue
            for i in seen_and_size:
                dir = i[0]
                # print(i)
                # print(current_dir)
                # print(dir)
                if dir == current_dir[:len(dir)]:
                    # print(args[0])
                    print(i[1])
                    i[1] += int(args[0])
                
            
        print('h',seen_and_size)            
part2_second('2022/day7test.txt')
            