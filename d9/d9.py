tail = (0,0)
visited = set()
visited.add(tail)
head = (0,0)

def neighbours(t):
    return [(t[0]+1,t[1]+1),(t[0],t[1]+1),(t[0]-1,t[1]+1),(t[0]+1,t[1]),(t[0],t[1]),(t[0]-1,t[1]),(t[0]+1,t[1]-1),(t[0],t[1]-1),(t[0]-1,t[1]-1)]

def movetail(h,t):
    if t in neighbours(h):
        return t
    if t[0] == h[0]:
        if t[1] == (h[1] + 2):
            return((h[0],h[1]+1))
        if t[1] == (h[1] - 2):
            return((h[0],h[1]-1))

    if t[1] == h[1]:
        if t[0] == (h[0] + 2):
            return((h[0]+1,h[1]))
        if t[0] == (h[0] - 2):
            return((h[0]-1,h[1]))

    #tail is not in row or col of head
    if t[0] > h[0]:
        xdir = -1
    else:
        xdir = 1
    if t[1] > h[1]:
        ydir = -1
    else:
        ydir = 1
    return((t[0]+xdir,t[1]+ydir))

for line in open("input.txt"):
    line = line.strip().split(" ")
    amt = int(line[1])
    if line[0] == "R":
        direction = (1,0)
    if line[0] == "L":
        direction = (-1,0)
    if line[0] == "U":
        direction = (0,1)
    if line[0] == "D":
        direction = (0,-1)

    for i in range(amt):
        head = (head[0] + direction[0], head[1]+direction[1])
        tail = movetail(head,tail)
        visited.add(tail)

print(len(visited))





