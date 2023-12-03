with open("day2.txt") as f:
    txt = [x.split(":") for x in f.read().split("\n")]

games = dict()
for line in txt:
    game_number = int(line[0].split(" ")[1])

    rounds = []
    pre = [x.strip().split(", ") 
           for x in line[1].strip().split(";")]

    for round in pre:
        r = dict()
        for color in round:
            a,b = color.split()
            r[b]=int(a)
        rounds.append(r)
    games[game_number] = rounds

# Determine which games would have been possible if 
# the bag had been loaded with only 
# 12 red cubes,
# 13 green cubes, and 
# 14 blue cubes. 
# What is the sum of the IDs of those games?

s = 0
limits = {"red": 12, "green": 13, "blue": 14}

for game in games:
    possible = True
    for round in games[game]:
        for color in round:
            possible = possible and (round[color] <= limits[color])
    if possible:
        s += game

print(s)

s = 0
r = 'red'
g = 'green'
b = 'blue'
for game in games:
    possible = {r: 0, g: 0, b: 0}
    for round in games[game]:
        for color in round:
            if round[color] > possible[color]:
                possible[color] = round[color]
    s += possible[r] * possible[g] * possible[b]

print(s)
