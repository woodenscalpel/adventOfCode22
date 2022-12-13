f = open("input.txt").readlines()

class monkey():
    def __init__(self,monkeyparse):
        self.id = int(monkeyparse[0].split(" ")[1][0])
        self.items = [int(x) for x in monkeyparse[1].strip().split(":")[1].split(",")]
        self.operation = monkeyparse[2].split("=")[1][5]
        self.delta = monkeyparse[2].split("=")[1][7:]
        self.divisor = int(monkeyparse[3].strip().split("by")[1])
        self.tpass =int(monkeyparse[4].split(" ")[-1])
        self.fpass =int(monkeyparse[5].split(" ")[-1])

        self.inspectCount = 0

    def initItems(self):
        newitems = []
        for item in self.items:
            newitems.append([item%x for x in _DIVISORS])
        self.items = newitems
    def turn(self):
        for item in self.items:
            #print("INSPECTING ", item)
            self.inspectCount += 1
            item = self.operate(item)
            #print("NEWITEM", item)
            #item = int(item/3)         ###PART 1
            flag = False
            if item[self.id]  == 0:
                #print("TRUE TROW TO", self.tpass)
                _MONKEYS[self.tpass].catch(item)
            else:
                #print("FALE TROW TO", self.fpass)
                _MONKEYS[self.fpass].catch(item)
        self.items = []

    def operate(self,item):
        #print(item)
        if self.delta == "old\n":
            delta = item
            return [(i*i)%m for i,m in zip(item,_DIVISORS)]
        else:
            delta = int(self.delta)

        if self.operation == "+":
            return [(i+delta)%m for i,m in zip(item,_DIVISORS)]
        else:
            return [(i*delta)%m for i,m in zip(item,_DIVISORS)]

    def catch(self,item):
        self.items.append(item)


parsemonkeys = [f[i:i+6] for i in range(0,len(f),7)]

_MONKEYS = []

for m in parsemonkeys:
    _MONKEYS.append(monkey(m))

_DIVISORS = [m.divisor for m in _MONKEYS]
print(_DIVISORS)
for m in _MONKEYS:
    m.initItems()

for _round in range(10000):
    print("ROUND",_round)
    for m in _MONKEYS:
        #print("MONKEY",m.id)
        m.turn()
    
activity = sorted([m.inspectCount for m in _MONKEYS])
print(activity[-2]*activity[-1])


