nums = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def replace_all(a: str):
    i = 0
    length = len(a)
    while i < length:
        if a[i] in '1234567890':
            i += 1
            continue
        for num in nums:
            if a[i:i+len(num)] == num:
                a = a.replace(num, nums[num] + num[-1])
                length = len(a)
                i += 1
                break
        else:
            i += 1
    return a
    

with open("day1.txt") as f:
    txt = f.read().split("\n")
    txt = [''.join([a for a in line if a in '1234567890']) for line in txt]
    for i, a in enumerate(txt):
        txt[i] = a[0] + a[-1]
    txt = [int(a) for a in txt]

with open("day1.txt") as f:
    txt2 = f.read().strip().split("\n")
#     txt2 = '''two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen'''.strip().split("\n")
#     txt2 = '''1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet'''.strip().split("\n")
    txt2 = [replace_all(a) for a in txt2]
    txt2 = [''.join([a for a in line if a in '1234567890']) for line in txt2]
    for i, a in enumerate(txt2):
        txt2[i] = a[0] + a[-1]
    txt2 = [int(a) for a in txt2]
    print(txt2[990])
    with open("out.txt", "w") as out:
        for line in ([str(x) for x in txt2]):
            out.write(line)
            out.write('\n')    
print(sum(txt))
print(sum(txt2))
