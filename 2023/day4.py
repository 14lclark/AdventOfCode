with open("day4.txt") as f:
    txt = [x.split(":") for x in f.read().strip().split("\n")]
    
for x in txt:
    while x[-1] != x[-1].replace("  ", " "):
        x[-1] = x[-1].replace("  ", " ")
cards = {int(a.split(" ")[-1]): [x.strip().split(" ") for x in b.strip().split("|")] for a, b in txt}

s = 0
num_winning = 0
num_of_cards = {x:1 for x in cards}
for card in cards:
    for win_num in cards[card][0]:
        for num in cards[card][1]:
            if win_num == num:
                num_winning += 1      
    for i in range(1,num_winning+1):
        num_of_cards[i+card] += num_of_cards[card]
    s += 2 ** (num_winning - 1) if num_winning > 0 else 0
    num_winning = 0
print(s)
s = 0
for x in num_of_cards:
    s += num_of_cards[x]
print(s)