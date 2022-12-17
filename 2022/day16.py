# pressure release valve
class Graph:
    def __init__(self, connections):
        if connections is None:
            self.vertices = {}
def make_connections(txt):
    connections = {}
    with open(txt) as f:
        for line in f:
            tokens = line.rstrip().split()
            rate = int(tokens[4].strip(';').split('=')[1])
            tunnels = [i.strip(', ') for i in tokens[9:]]
            connections[tokens[1]] = {'rate': rate, 'tunnels': tunnels}
    return connections

def search(graph: dict, start: str, time_left: int, released=0, open: list=None):
    if time_left == 1:
        if start not in open:
            return released, [open]
        return released, ['walk']

    steps = []
    total_pressure = 0
    if open is None:
        open = list()
    options = []
    max_pressure = 0
    new_steps = []
    for next in graph[start]['tunnels']:
        option = search(graph, next, time_left-1, open=(open + [start]))
        if option[0] > max_pressure:
            max_pressure = option[0]
            new_steps = option[1]    

        for second_step in graph[next]['tunnels']:
            option = search(graph, next, time_left-2, open=(open))
            if option[0] > max_pressure:
                max_pressure = option[0]
                if time_left - 2 > 0:
                    new_steps = ['walk'] + option[1] 
                else:
                    new_steps = []

    total_pressure = calc_total_pressure(new_steps, graph, time_left)
    return total_pressure, new_steps

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

    return search(connections_prime,"AA",30)
    ## Test calc_total_pressure
    # w = 'walk'
    # A = 'AA'
    # B = "BB"
    # C = "CC"
    # D = "DD"
    # E = "EE"
    # F = "FF"
    # G = "GG"
    # H = "HH"
    # I = "II"
    # J = "JJ"
    # return calc_total_pressure([w, D, w, w, B, w, w, w, J, \
    #                     w, w, w, w, w, w, w, H, w, w, \
    #                     w, E, w, w, C], connections, 30)
    
    
print(part1('2022/day16test.txt'))