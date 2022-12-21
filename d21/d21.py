f = open("input.txt").readlines()
m1 = [line.strip().split(":") for line in f]
monkeys = {}
for m in m1:
    try:
        int(m[1])
        monkeys[m[0]] = int(m[1])
    except:
        monkeys[m[0]] = m[1].strip().split(" ")

print(monkeys)

def monkeyeval(monkeys,monkeyname):
    print("eval",monkeyname)
    if type(monkeys[monkeyname]) == int:
        print("int",monkeys[monkeyname])
        return monkeys[monkeyname]
    else:
        firstarg = monkeyeval(monkeys,monkeys[monkeyname][0])
        secondarg = monkeyeval(monkeys,monkeys[monkeyname][2])

        op = monkeys[monkeyname][1]
        if op == '+':
            return firstarg + secondarg
        if op == '-':
            return firstarg - secondarg
        if op == '*':
            return firstarg * secondarg
        if op == '/':
            return firstarg / secondarg
print(monkeyeval(monkeys,'root'))
