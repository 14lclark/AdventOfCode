# rock paper scissors tournament 

# AX rock
# BY paper
# CZ scissors
possibilities = {'A': 1, 'X': 1, 'B': 2, 'Y': 2, 'C': 3, 'Z': 3}
def part1():
    
    def winner(x):
        p1,p2 = x[0],x[1]
        val = possibilities[p1] * possibilities[p2]
        if val == 2: 
            return 2
        if val == 3:
            return 1
        if val == 6:
            return 3
        return 0

    with open('2022/day2.txt') as f:
        total = 0
        for line in f:
            
            players = line.split()
            move = possibilities[players[1]]
            score = move
            win = winner(players)
            if win == move:
                score += 6
            if win == 0:
                score += 3       
            total += score
    print(total)
    
def part2():
    losepairs = {1: 2, 2: 3, 3: 1}
    winpairs = {2: 1, 3: 2, 1: 3}
    def winnerloser(p1):
        #returns (x,y) where x beats p1 and y loses to p1
        p = possibilities[p1]
        return (winpairs[p], losepairs[p])
    
    total = 0
    with open('2022/day2.txt') as f:
        for line in f:
            score = 0
            inputs = line.split()
            enemy = inputs[0]
            strat = inputs[1]
            if strat == 'X': # my loss = enemy win
                score += winpairs[possibilities[enemy]]
            if strat == 'Y': # draw, means enemy and i played the same move
                score += 3
                score += possibilities[enemy]
            if strat == 'Z': # my win = enemy loss
                score += 6
                score += losepairs[possibilities[enemy]]
            total += score
    print(total)
    
part2()
    