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
    
# print(part1('2022/day16.txt', "AA", 30))

def path_from_prev(prev: dict, source, target):
    path = []
    if target == source: 
        return path
    if prev[target] == source:
        return [target]

    t, s = target, source

    while t != source:
        path = [t] + path
        t = prev[t]
    
    return path
        
def path_to_next(connections, dist_prev, source, \
               closed, time_left):
    dist, prev_in_path = dist_prev
    max_released = 0
    max_score = 0
    max_valve = None
    for valve in closed:
        rate = connections[valve]['rate']
        distance = dist[valve]
        # print(distance)
        if distance + 1 >= time_left:
            continue
    
        released = rate * (time_left - distance - 1 )
        score = released / distance**2
        # print(score)
        if score > max_score:
            max_released = released
            max_score = score
            max_valve = valve
        # print(f'{valve, max_released=}') 
        print(max_valve)  
    if max_valve == None:
        return None
    
    closed.remove(max_valve)
    return path_from_prev(prev_in_path, source, max_valve)
    # if max_valve is None:
    #     break
    # else:
    #     closed.remove(max_valve)


def part2(txt, start, total_time):
    connections = make_connections(txt)
    print(connections)
    source = start
    closed = [i for i in connections if connections[i]['rate'] != 0]
    total_released_pressure = 0

    ppl = {'me':  {'pos': source, 'dest': None, 'path': []}} \
                #'ele': {'pos': source, 'dest': None, 'path': []}}
    total_rate = 0
    added_rates = 0
    time = 1
    for p in ppl:
        pos = ppl[p]['pos']
        dist_prev = \
            dijkstra_shortest_path(connections,pos)
        ppl[p]['path'] = \
            path_to_next(connections, dist_prev, pos, \
                         closed, total_time - time)
        ppl[p]['dest'] = ppl[p]['path'][-1]  
        # closed.remove(ppl[p]['path'][-1])   

    

    completed = []
    open_valves = []

    print(ppl)
    while time <= total_time:
        print(f"== Minute {time} ==")
        total_rate += added_rates

        if not open_valves:
            print("No valves are open.")
        else:
            x = "Valves " + ', '.join(open_valves[:-1]) + ', and ' + str(open_valves[-1] + " are")
            if len(open_valves) == 1:
                x = "Valve " + str(open_valves[0] + " is")
            if len(open_valves) == 2:
                x = "Valves " + str(open_valves[0]) + " and " + str(open_valves[1] + " are")
            print(f"{x} open, releasing {total_rate} pressure.")

        total_released_pressure += total_rate
        added_rates = 0
        for person in ppl:
            if person in completed:
                continue
     
            if ppl[person]['path'] is None:
                completed.append(person)
                continue
            
            ppl[person]['pos'] = ppl[person]['path'][0]
            ppl[person]['path'].remove(ppl[person]['pos'])                

            pos = ppl[person]['pos']
            dest = ppl[person]['dest']            
            if pos == dest:
                open_valves.append(dest)
                added_rates += connections[pos]['rate']
                dist_prev = \
                    dijkstra_shortest_path(connections,pos)
                ppl[person]['path'] = \
                    path_to_next(connections, dist_prev, pos, \
                                 closed, total_time - time)     

                ppl[person]['dest'] = ppl[person]['path'][-1]
                # closed.remove(ppl[person]['dest'])
        # print(f'{time, added_rates, total_rate=}')
        time += 1
    return total_released_pressure

print(part2('2022/day16test.txt', "AA", 26))