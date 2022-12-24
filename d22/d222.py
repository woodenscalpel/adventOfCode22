m = {}
#0-49,50-99,100-149
#Some hardcoding of edges (+1 because checking at NEXT position)
#Cube looks like this
# 21
# 3
#54
#6
#Right,Left,Top,Bottom
SIDELENGTH=50

T1 = [(100+x,-1) for x in range(SIDELENGTH)]
R1 = [(150,0+y) for y in range(SIDELENGTH)]
B1 = [(100+x,50) for x in range(SIDELENGTH)]
T2 = [(50+x,-1) for x in range(SIDELENGTH)]
L2 = [(49,0+y) for y in range(SIDELENGTH)]
L3 = [(49,50+y) for y in range(SIDELENGTH)]
T5 = [(0+x,99) for x in range(SIDELENGTH)]
L5 = [(-1,100+y) for y in range(SIDELENGTH)]
L6 = [(-1,150+y) for y in range(SIDELENGTH)]
B6 = [(0+x,200) for x in range(SIDELENGTH)]
R6 = [(50,150+y) for y in range(SIDELENGTH)]
B4 = [(50+x,150) for x in range(SIDELENGTH)]
R4 = [(100,100+y) for y in range(SIDELENGTH)]
R3 = [(100,50+y) for y in range(SIDELENGTH)]
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
            return npos,d
        if m[npos] == True: #dont move if wall
            return p,d
    else:
        npos,d2 = wraparound(npos,d)
        if m[npos] == False:
            print("PRE WRAP (pos, dir)", p,d)
            print("POST WRAP (pos,dir)", npos,d2)
            return npos,d2
        if m[npos] == True: #dont move if wall
            return p,d

    
def wraparound(position,direction):
    xpos,ypos = position
    "hardcoded edges :)"
    if position in B1 and direction == (0,1):
        newdir = (-1,0)
        idx = xpos % 50
        newpos = (99,50+idx)
    if position in R1 and direction == (1,0):
        newdir = (-1,0)
        idx = ypos % 50
        idx = abs(idx-49)
        newpos = (99,100+idx)
    if position in T1 and direction == (0,-1):
        newdir = (0,-1)
        idx = xpos % 50
        newpos = (0+idx,199)
    if position in T2 and direction == (0,-1):
        newdir = (1,0)
        idx = xpos % 50
        newpos = (0,150+idx)
    if position in L2 and direction == (-1,0):
        newdir = (1,0)
        idx = ypos % 50
        idx = abs(idx-49)
        newpos = (0,100+idx)
    if position in L3 and direction == (-1,0):
        newdir = (0,1)
        idx = ypos % 50
        newpos = (0+idx,100)
    if position in T5 and direction == (0,-1):
        newdir = (1,0)
        idx = xpos % 50
        newpos = (50,50+idx)
    if position in L5 and direction == (-1,0):
        newdir = (1,0)
        idx = ypos % 50
        idx = abs(idx-49)
        newpos = (50,0+idx)
    if position in L6 and direction == (-1,0):
        newdir = (0,1)
        idx = ypos % 50
        newpos = (50+idx,0)
    if position in B6 and direction == (0,1):
        newdir = (0,1)
        idx = xpos % 50
        newpos = (100+idx,0)
    if position in R6 and direction == (1,0):
        newdir = (0,-1)
        idx = ypos % 50
        newpos = (50+idx,149)
    if position in B4 and direction == (0,1):
        newdir = (-1,0)
        idx = xpos % 50
        #idx = abs(idx-49)    THIS LINE COST ME 2 HOURS
        newpos = (49,150+idx)
    if position in R4 and direction == (1,0):
        newdir = (-1,0)
        idx = ypos % 50
        idx = abs(idx-49)
        newpos = (149,0+idx)
    if position in R3 and direction == (1,0):
        newdir = (0,-1)
        idx = ypos % 50
        newpos = (100+idx,49)
    #print(newpos)
    return [newpos,newdir]

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
            position,direction = move(position,direction)
            #print(position,direction)
    else: #L or R
        direction = rotate(direction,i)
print((position[0]+1)*4,(position[1]+1)*1000,direction)
