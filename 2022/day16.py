# pressure release valve

def make_connections(txt):
    connections = {}
    with open(txt) as f:
        for line in f:
            tokens = line.rstrip().split()
            rate = int(tokens[4].strip(';').split('=')[1])
            neighbors = [i.strip(', ') for i in tokens[9:]]
            connections[tokens[1]] = {'rate': rate, 'neighbors': neighbors}
    return connections

def dijkstra_shortest_path(graph: dict, source) -> list:
    prev = []
    distance_to_source = {i: len(graph) + 10 for i in graph}
    distance_to_source[source] = 0
    prev_in_shortest_path = {}
    vertices = [v for v in graph]
    while len(vertices):
        closest = min(vertices, key=distance_to_source.get)
        vertices.remove(closest)

        for neighbor in set(graph[closest]['neighbors']) & set(vertices):
            alt_dist = distance_to_source[closest] + 1
            if alt_dist < distance_to_source[neighbor]:
                distance_to_source[neighbor] = alt_dist
                prev_in_shortest_path[neighbor] = closest

    
    return distance_to_source, prev_in_shortest_path
    

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


def part1(txt, start, total_time):
    connections = make_connections(txt)
    print(connections)
    source = start
    time_left = total_time
    closed = [i for i in connections if connections[i]['rate'] != 0]
    total_released_pressure = 0

    while time_left > 0:
        dist, prev_in_path = \
            dijkstra_shortest_path(connections,source)
        max_released = 0
        max_score = 0
        max_valve = None
        for valve in closed:
            rate = connections[valve]['rate']
            distance = dist[valve]
            # print(distance)
            if not rate:
                continue
            if distance >= time_left:
                continue
        
            released = rate * (time_left - distance - 1 )
            score = released / distance**2
            print(score)
            if score > max_score:
                max_released = released
                max_score = score
                max_valve = valve
            print(f'{valve, max_released=}')        
        if max_valve is None:
            break
        else:
            closed.remove(max_valve)

        time_left -= dist[max_valve] + 1
        print(max_valve)
        print(time_left)
        total_released_pressure += max_released
        source = max_valve
    print(closed)
    return total_released_pressure
    
print(part1('2022/day16.txt', "AA", 30))