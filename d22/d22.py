m = {}
for y,line in enumerate(open("input.txt").readlines()):
    for x,char in enumerate(line):
        if char == ".":
            m[(x,y)] = False
        if char == "#":
            m[(x,y)] = True

def rotate(d,clock):
    #clock is R or L
    #should have made a dict lol
    if clock == 'R':
        if d == (1,0): return (0,1)
        if d == (0,1): return (-1,0)
        if d == (-1,0): return (0,-1)
        if d == (0,-1): return (1,0)
    if clock == 'L':
        if d == (1,0): return (0,-1)
        if d == (0,-1): return (-1,0)
        if d == (-1,0): return (0,1)
        if d == (0,1): return (1,0)

def tadd(t1,t2): return (t1[0]+t2[0],t1[1]+t2[1])

def move(p,d): #pos,dir
    npos = tadd(p,d)
    if npos in m:
        if m[npos] == False:
            return npos
        if m[npos] == True: #dont move if wall
            return p
    else:
        npos = wraparound(p,d)
        print("wrap returned", npos)
        if m[npos] == False:
            return npos
        if m[npos] == True: #dont move if wall
            return p

    
def wraparound(position,direction):
    """
    Assumming called correctly. Depending on dir finds the wrapped pos
    ex dir (1,0) finds first in line, dir(-1, 0) last
    """
    print("WRAPPING",position,direction)
    bounds = 999 # a big number
    if direction == (1,0):
        for x in range(bounds):
            if (x,position[1]) in m:
                return (x,position[1])
    if direction == (-1,0):
        for x in reversed(range(bounds)):
            if (x,position[1]) in m:
                return (x,position[1])
    if direction == (0,-1):
        for y in reversed(range(bounds)):
            if (position[0],y) in m:
                return (position[0],y)
    if direction == (0,1):
        for y in range(bounds):
            if (position[0],y) in m:
                return (position[0],y)

for i in range(100):
    if (i,0) in m:
        startpos = (i,0)
        break
startdir = (1,0)

instructions = open('inputinstructions.txt').read()
instructionlist = []
acc = ""
for char in instructions:
    if char == "L":
        if acc != 0: instructionlist.append(int(acc))
        instructionlist.append('L')
        acc = ""
    elif char == "R":
        if acc != 0: instructionlist.append(int(acc))
        instructionlist.append('R')
        acc = ""
    elif char == "\n":
        if acc != 0: instructionlist.append(int(acc))
    else:
        acc += char

position = startpos
direction = startdir
for i in instructionlist:
    if type(i) == int:
        for mov in range(i):
            position = move(position,direction)
            print(position)
    else: #L or R
        direction = rotate(direction,i)
print(position,direction)
print((position[0]+1)*4,(position[1]+1)*1000,direction)

