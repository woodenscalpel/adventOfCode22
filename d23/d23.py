#Directions
N,E,S,W = 0,1,2,3
f = open("input.txt")

def neighbours(pos):
    x,y = pos
    n = []
    for i in range(-1,2):
        for j in range(-1,2):
            if i != 0 or j != 0:
                n.append((x+i,y+j))
    return n

def emptydirneighbours(elves,pos):
    Nmov = Smov = Emov = Wmov = False
    x,y = pos
    if (x-1,y-1) not in elves and (x,y-1) not in elves and (x+1,y-1) not in elves: Nmov = True
    if (x+1,y-1) not in elves and (x+1,y) not in elves and (x+1,y+1) not in elves: Emov =  True
    if (x-1,y+1) not in elves and (x,y+1) not in elves and (x+1,y+1) not in elves: Smov = True
    if (x-1,y-1) not in elves and (x-1,y) not in elves and (x-1,y+1) not in elves: Wmov = True
    return [Nmov,Emov,Smov,Wmov]

elves = {}
y = 0
for line in f.readlines():
    x = 0
    for char in line:
        if char == '#': elves[(x,y)] = False
        x += 1
    y+=1


def doround(elves,directions):
    moved = False
    #Propose Moves
    for elf in elves:
        #print("looking at elf", elf)
        trymove = False
        for n in neighbours(elf):
            if n in elves:
                trymove = True
                break

        if trymove == True:
            #print("wants to move!")
            moverules = emptydirneighbours(elves,elf)
            #print(moverules)
            for d in directions:
                if moverules[d] == True:
                    if d == N:
                        #print("N")
                        elves[elf] = (elf[0],elf[1]-1)
                    if d == S:
                        #print("S")
                        elves[elf] = (elf[0],elf[1]+1)
                    if d == E:
                        #print("E")
                        elves[elf] = (elf[0]+1,elf[1])
                    if d == W:
                        #print("W")
                        elves[elf] = (elf[0]-1,elf[1])
                    break
    #Execute moves
    for elf in list(elves):
        if elves[elf]:
            currentpos = elf
            targetmove = elves[elf]
            #Check neighbours of target move (except this elf) and see if any of them also want to move here
            executemove = True
            for n in neighbours(targetmove):
                if n != currentpos:
                    if n in elves and elves[n] == targetmove:
                        executemove = False
            #execute move
            if executemove:
                moved = True
                del elves[currentpos]
                elves[targetmove] = False
    #Reset elves to false for next step
    for elf in list(elves):
        elves[elf] = False
    return [elves,moved]

def visual(elves):
    for y in range(0,12):
        line = ""
        for x in range(0,14):
            if (x,y) in elves:
                line += '#'
            else: line += '.'
        print(line)


def rectangle(elves):
    minx = 99999
    maxx = -9999
    miny = 9999
    maxy = -9999
    for elf in elves:
        x,y = elf
        if x > maxx: maxx = x
        if x < minx: minx = x
        if y > maxy: maxy = y
        if y < miny: miny = y

    print((maxx-minx+1)*(maxy-miny+1) - len(elves))

directions = [N,S,W,E]
#print(elves)
visual(elves)
moved = True
r = 0
while moved == True:
    elves,moved  = doround(elves,directions)
    directions = directions[1:] + [directions[0]]
    #print(directions)
    #print(elves)
    #visual(elves)
    if r == 9:
        print("Silver: ",rectangle(elves))
    r += 1
print(r)

