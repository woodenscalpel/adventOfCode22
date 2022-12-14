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

rocks = []
for inputline in f.readlines():
    lines = [[int(x) for x in l.split(",")] for l in inputline.strip().split("->")]
    for i in range(len(lines)-1):
        rocks.extend(drawline(lines[i],lines[i+1]))

FLOOR = 166 + 2 #hardcoded
#FLOOR = 11
rocks.extend(drawline([-5000,FLOOR],[5000,FLOOR]))

p2sand = set()

nextx = [500]
for y in range(0,FLOOR):
    nexterx = set()
    for x in nextx:
        #print("DROPPING SAND AT", x, y)
        #print("DROPPING SAND AT", x, y)
        if [x,y+1] not in rocks:
            p2sand.add((x,y+1))
            nexterx.add(x)
        if [x-1,y+1] not in rocks:
            p2sand.add((x-1,y+1))
            nexterx.add(x-1)
        if [x+1,y+1] not in rocks:
            p2sand.add((x+1,y+1))
            nexterx.add(x+1)
    nextx = nexterx

print(len(p2sand)+1)
