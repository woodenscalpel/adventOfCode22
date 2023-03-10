f = open("input.txt")
bigacc = 0
for line in f.readlines():
    digits  = list(line.strip())
    print("===")
    acc = 0
    for idx,digit in enumerate(reversed(digits)):
        if digit == "=": digit = -2
        if digit == "-": digit = -1
        acc += (5**idx)*int(digit)
    print(acc)
    bigacc += acc
print("=====")
print(bigacc)
print("2=-1=0")

def decode(snafu):
    digits  = list(snafu.strip())
    acc = 0
    for idx,digit in enumerate(reversed(digits)):
        if digit == "=": digit = -2
        if digit == "-": digit = -1
        acc += (5**idx)*int(digit)
    return acc


def bruteforce(beginning):
    acc = []
    for item in beginning:
        for i in range(-2,3):
            if i == -2:
                d = "="
            elif i == -1:
                d = "-"
            else:
                d = str(i)
            acc.append(item+d)
    return acc
        
"""
acc = [""]
for i in range(5):
    acc = bruteforce(acc)
print("_____")
print(bigacc)

for i in range(100):
    for item in acc:
        if decode(item) == i:
            print(i,item)
"""
iacc = 0
for i in range(25):
    ans = (bigacc+iacc)/5**i
    print(int(ans%5))
    iacc += (5**i)*2

