y = 0
blizz = {}
for line in open("input.txt"):
    line = line.strip()
    x = 0
    for char in line:
        if char != '.' and char != '#':
            blizz[(x,y)] = [char]
        x += 1
    maxx = x - 2
    y +=1
maxy = y-2
#Game board is from 1 - maxx x, 1 - maxy y
print(maxx,maxy)

def moveblizz(pos,char):
    x,y = pos
    if char == '^':
        pos = (x,y-1)
        if y-1 == 0:
            pos = (x,maxy)
    if char == '>':
        pos = (x+1,y)
        if x+1 == maxx+1:
            pos = (1,y)
    if char == 'v':
        pos = (x,y+1)
        if y+1 == maxy+1:
            pos = (x,1)
    if char == '<':
        pos = (x-1,y)
        if x-1 == 0:
            pos = (maxx,y)
    return pos,char

def addblizz(blizz,pos,char):
    if pos not in blizz:
        blizz[pos] = [char]
    else:
        blizz[pos].append(char)

def stepblizz(blizz):
    newblizz = {}
    for b in blizz:
        for b1 in blizz[b]:
            newpos,char = moveblizz(b,b1)
            addblizz(newblizz,newpos,char)
    return newblizz

def visual(blizz):
    for y in range(0,maxy+2):
        line = ""
        for x in range(0,maxx+4):
            if (x,y) in blizz:
                line += blizz[(x,y)][0]
            else: line += '.'
        print(line)

def neighbours(pos):
    #return neighbours and self (for waiting):
    x,y = pos
    npos = [pos]
    if x < maxx and y > 0: npos.append((x+1,y))
    if x > 1 and (y-1) < maxy: npos.append((x-1,y))
    if y < maxy: npos.append((x,y+1))
    if y > 1: npos.append((x,y-1))
    if (x,y+1) == END: npos.append(END)
    if (x,y-1) == START: npos.append(START)
    return npos
            


START = (1,0)
END = (maxx,maxy+1) 

states = [START]

positions = START
t = 0
while True:
    t = t+1
    blizz = stepblizz(blizz)
    newstates = set()
    for state in states:
        for nstate in neighbours(state):
            if nstate not in blizz:
                newstates.add(nstate)
    states = newstates
    if END in newstates:
        print(t)
        break
 
states = [END]

while True:
    t = t+1
    blizz = stepblizz(blizz)
    newstates = set()
    for state in states:
        for nstate in neighbours(state):
            if nstate not in blizz:
                newstates.add(nstate)
    states = newstates
    print(states)
    if START in newstates:
        #print(t)
        break

states = [START]

while True:
    t = t+1
    blizz = stepblizz(blizz)
    newstates = set()
    for state in states:
        for nstate in neighbours(state):
            if nstate not in blizz:
                newstates.add(nstate)
    states = newstates
    if END in newstates:
        print(t)
        break

print((END))
