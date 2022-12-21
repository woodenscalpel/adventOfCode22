m1 = [line.strip().split(":") for line in open("input.txt").readlines()]
monkeys = {}
for m in m1:
    try:    monkeys[m[0]] = int(m[1])
    except: monkeys[m[0]] = m[1].strip().split(" ")

def monkeyeval(monkeys,monkeyname):
    if type(monkeys[monkeyname]) == int: return monkeys[monkeyname]
    else:
        firstarg  = monkeyeval(monkeys,monkeys[monkeyname][0])
        secondarg = monkeyeval(monkeys,monkeys[monkeyname][2])
        if monkeyname == 'root':
            return [firstarg,secondarg]

        match monkeys[monkeyname][1]:
            case '+': return firstarg + secondarg
            case '-': return firstarg - secondarg
            case '*': return firstarg * secondarg
            case '/': return firstarg / secondarg

def fx(monkeys,x0):
    monkeys['humn'] = x0
    return monkeyeval(monkeys,'root')

#Newtons Method
x0 = 100000
error = 999
while abs(error) > 0:
    [ans,goal] = fx(monkeys,int(x0))
    error = ans - goal
    dx = (fx(monkeys,int(x0+1))[0]-fx(monkeys,int(x0-1))[0])/2
    x0 = int(x0 - error/dx)
print(x0)

