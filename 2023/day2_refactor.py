games = {}
for line in (f:=open("day2.txt")):
    line = line.split(":")
    game_number = int(line[0].split(" ")[1])
    rounds = []
    pre = [x.strip().split(", ") 
           for x  in line[1].strip().split(";")]
    for round in pre:
        r = {}
        for color in round:
            a, b = color.split()
            r[b] = int(a)
        rounds.append(r)
    games[game_number] = rounds
f.close()
s1 = 0
s2 = 0
r,g,b = 'red','green','blue'
limits = {r: 12, g: 13, b: 14}
for game in games:
    possible = True
    needed = {r: 0, g: 0, b: 0}
    for round in games[game]:
        for color in round:
            possible = possible and (round[color] <= limits[color])
            if round[color] > needed[color]:
                needed[color] = round[color]
    if possible:
        s1 += game
    s2 += needed[r] * needed[g] * needed[b]
print(s1, s2)