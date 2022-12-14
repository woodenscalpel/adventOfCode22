f = open("input.txt")
import sys
sys.setrecursionlimit(100000) #lol



def drawline(p1,p2):
    rocklist = []
    if p1[0] == p2[0]:
        if p1 < p2:
            for i in range(p1[1],p2[1]+1):
                rocklist.append([p1[0],i])
        if p2 < p1:
            for i in range(p2[1],p1[1]+1):
                rocklist.append([p1[0],i])

    if p1[1] == p2[1]:
        if p1 < p2:
            for i in range(p1[0],p2[0]+1):
                rocklist.append([i,p1[1]])
        if p2 < p1:
            for i in range(p2[0],p1[0]+1):
                rocklist.append([i,p1[1]])
    return rocklist

def dropsand(x,y):
    #print("DROPPING SAND AT", x, y)
    if y == 1000: #sand fell off map
        return 0
    if [x,y+1] in rocks:
        #print(x,y+1, "IN ROCKS")
        if [x-1,y+1] in rocks:
            #print(x-1,y+1,"LEFT IS ROCK")
            if [x+1,y+1] in rocks:
                #print(x+1,y+1,"RIGHT IS ROCK")
                return [x,y]
            else:
                #print("DROPPING RIGHT")
                return dropsand(x+1,y+1)
        else:
            #print("DROPPING LEFT")
            return dropsand(x-1,y+1)
    else:
        #sand sucessfully drops
        #print("DROPPING DOWN")
        return dropsand(x,y+1)


rocks = []
for inputline in f.readlines():
    lines = [[int(x) for x in l.split(",")] for l in inputline.strip().split("->")]
    for i in range(len(lines)-1):
        rocks.extend(drawline(lines[i],lines[i+1]))

#print(rocks)
coord = -1
accum = 0
while coord != 0:
    coord = dropsand(500,0)
    print(coord)
    if coord != 0:
        rocks.append(coord)
        #print(rocks)
        #print(len(rocks))
        accum += 1
print(accum)
