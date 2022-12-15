# make space on communication device

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
            
def dir_str(dir):
    acc = ''
    for i in dir:
        acc += i + '/'
    return acc

def directories_and_sizes(txt) -> dict:
    with open(txt) as f:
        current_dir = []
        
        # [dir, size]
        seen_and_size = {}
        for line in f:
            args = line.split()
            if args[0] == '$':
                if args[1] == 'cd':
                    if args[2] == '/':
                        current_dir = ['top']
                        if dir_str(current_dir) not in seen_and_size.keys():
                            seen_and_size["top/"] = 0

                    elif args[2] == '..':
                        current_dir.pop()
                        
                    else:
                        # print(args[2])
                        current_dir.append(args[2])
                        if dir_str(current_dir) not in seen_and_size.keys():
                            seen_and_size[dir_str(current_dir)] = 0     
                    continue
                if args[1] == 'ls':
                    continue
            if args[0] == 'dir':
                continue
            for dir in seen_and_size:
                
                # print(i)
                # print(current_dir)
                # print(dir)
                if dir in dir_str(current_dir):
                    # print(args[0])
                    seen_and_size[dir] += int(args[0])
        return(seen_and_size)

def part1(txt, max_size):
    dir_sizes = directories_and_sizes(txt)
    count = 0
    for dir, size in dir_sizes.items():
        if size <= max_size:
            count += size
    return count

def part2(txt, needed_size, file_system_size):
    dir_sizes = directories_and_sizes(txt)
    delete_size = needed_size - (file_system_size - dir_sizes['top/'])

    smallest = dir_sizes['top/']
    for size in dir_sizes.values():
        if size >= delete_size and size <= smallest:
            smallest = size
    return smallest

print('part1', part1('2022/day7.txt', 100_000))
print('part2', part2('2022/day7.txt', 30_000_000, 70_000_000))
        