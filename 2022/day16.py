# pressure release valve

def make_connections(txt):
    connections = {}
    with open(txt) as f:
        for line in f:
            tokens = line.rstrip().split()
            rate = int(tokens[4].strip(';').split('=')[1])
            tunnels = [i.strip(', ') for i in tokens[9:]]
            connections[tokens[1]] = {'rate': rate, 'tunnels': tunnels}
    return connections

def search(graph: dict, start, steps: list):
    while True:
        
        pass

def dijkstra_shortest_path(graph: dict, start, stop, max_steps=10) -> list:
    current = start
    
    distance_to_start = {i: -1 for i in graph}
    distance_to_start[start] = 0
    path_to_start = {start: []}
    for i in graph[current]['tunnels']:
        if 0 <= distance_to_start[i] <= distance_to_start[current]:
            continue
        
        distance_to_start[i] = distance_to_start[current] + 1
        path_to_start[i] = path_to_start[current].append(i)
        
    
        
        
    

def calc_total_pressure(steps, connections, total_time):
    total_released_pressure = 0
    total_rate = 0
    if steps[0] != 'walk':
        total_rate = steps[0]
    t = 1
    for i in steps[1:]:
        t+=1
        total_released_pressure += total_rate
        if i == 'walk':
            continue
        total_rate += connections[i]['rate']
    
    if len(steps) < total_time:
        total_released_pressure += total_rate * (total_time - t)
    
    return total_released_pressure
        
        
        
            
    

def part1(txt):
    connections = make_connections(txt)
    print(connections)
    dijkstra_shortest_path(connections, 'AA','HH', max_iters=10)
    
    
print(part1('2022/day16test.txt'))