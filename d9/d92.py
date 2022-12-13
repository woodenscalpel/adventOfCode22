head = (0,0)
one = (0,0)
two = (0,0)
three = (0,0)
four = (0,0)
five = (0,0)
six = (0,0)
seven = (0,0)
eight = (0,0)
tail = (0,0)
visited = set()
visited.add(tail)

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
        one = movetail(head,one)
        two = movetail(one,two)
        three = movetail(two,three)
        four = movetail(three,four)
        five = movetail(four,five)
        six = movetail(five,six)
        seven = movetail(six,seven)
        eight = movetail(seven,eight)
        tail = movetail(eight,tail)
        visited.add(tail)

print(len(visited))
