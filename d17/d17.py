import copy

rocks = []
rocks.append([(0,0),(1,0),(2,0),(3,0)]) #straight
rocks.append([(1,0),(0,1),(1,1),(1,2),(2,1)]) #cross
rocks.append([(0,0),(1,0),(2,0),(2,1),(2,2)]) #el
rocks.append([(0,0),(0,1),(0,2),(0,3)]) #straight v
rocks.append([(0,0),(1,0),(0,1),(1,1)]) #square

windfile = open("input.txt").readline().strip()
windpattern = []
for char in windfile:
    if char == ">":
        windpattern += [1]
    if char == "<":
        windpattern += [-1]
windlength = len(windpattern)
print(windpattern)

Rockcounter = 0 

MAXH= 0

MINW= 0
MAXW= 6

board = {}

def getnext(_id):
    currentpiece = copy.deepcopy(rocks[_id])
    for i in range(len(currentpiece)):
        currentpiece[i] = (currentpiece[i][0]+2,currentpiece[i][1]+MAXH+3)
    return currentpiece

def gravitycheck(currentpiece):
    #Gravity Step
    for tile in currentpiece:
        if tile[1]-1 == -1:
            return False
        if (tile[0],tile[1]-1) in board:
            return False
    return True

def windcheck(currentpiece,_dir):
    for tile in currentpiece:
        if (tile[0]+_dir,tile[1]) in board:
            return False

        if _dir == 1:
            if tile[0]+1 > MAXW:
                return False

        if _dir == -1:
            if tile[0]-1 < MINW:
                return False
    return True
 
def timestep(pid,currentpiece,wind,windidx):
    global MAXH
    global Rockcounter

    if windcheck(currentpiece,wind):
        for i in range(len(currentpiece)): currentpiece[i] = (currentpiece[i][0]+wind,currentpiece[i][1])

    if gravitycheck(currentpiece):
        #make peice fall
        for i in range(len(currentpiece)): currentpiece[i] = (currentpiece[i][0],currentpiece[i][1]-1)
    else:
        #Else peice becomes board and get next peice
        for item in currentpiece: 
            board[item] = 1
            if item[1] >= MAXH: 
                MAXH = item[1]+1
        pid = pid + 1
        Rockcounter += 1
        if pid == 5: pid = 0
        currentpiece = getnext(pid)
        if pid == 1 and windidx == 6:
            print("WIND AT 1",windidx,Rockcounter,MAXH)
        if windidx == 0 and pid == 0:
            print("CYCLE",MAXH)
        return [pid, currentpiece]
    return [pid,currentpiece]

currentpiece = getnext(0)
pid = 0
windidx = 0
heights = []
while Rockcounter < 3290: #OFFSET + REMAINDER
    wind = windpattern[windidx]
    windidx +=1
    if windidx > windlength-1: windidx = 0
    pid,currentpiece = timestep(pid,currentpiece,wind,windidx)
    heights.append([pid,MAXH])
    #print(currentpiece)
    #print(board)
print(MAXH)
