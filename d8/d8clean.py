#Make grid of [Height,Visible]
grid = [[[int(x),False] for x in line.strip()] for line in open("input.txt")]
GRIDSIZE = len(grid[0])

#Outside is visible
for i,row in enumerate(grid):
    for j,tree in enumerate(row):
        if i == 0 or j == 0 or i == GRIDSIZE - 1 or j == GRIDSIZE - 1:
            tree[1] = True

def look(grid,start,direction):
    #start from point, check if each tree has line of sight and if it is visible, going in given direction
    prevcoord = start
    prev = grid[start[0]][start[1]]
    visheight = prev[0]
    seen = 0

    while visheight < 9:
        newcoord = (prevcoord[0]+direction[0],prevcoord[1]+direction[1])
        new = grid[newcoord[0]][newcoord[1]]
        #if next point is on the edge, return
        if newcoord[0] == 0 or newcoord[0] == GRIDSIZE -1 or newcoord[1] == 0 or newcoord[1] == GRIDSIZE-1:
            return seen + 1
        # if next point is taller than previous visheight, tree is visible, tree height is new visheight
        if new[0] > visheight:
            grid[newcoord[0]][newcoord[1]][1] = True
            visheight = new[0]
        #if next point is smaller, tree is not visible but line of sight continues
        #new point is prev point
        prevcoord = newcoord
    return seen + 1

###PART 1###
#Look from edges
for row in range(1,GRIDSIZE-1):
    look(grid,(row,0),(0,1))
    look(grid,(row,GRIDSIZE-1),(0,-1))
for col in range(1,GRIDSIZE-1):
    look(grid,(0,col),(1,0))
    look(grid,(GRIDSIZE - 1,col),(-1,0))

#Add up visible trees
visible = 0
for row in grid:
    for tree in row:
        if tree[1] == True:
            visible += 1
print("PART 1: ",visible)

###PART 2###
#Modify look to be blocked at >= instead of greater, and return count of trees
def look2(grid,start,direction):
    #start from point, check if each tree has line of sight and if it is visible, going in given direction
    prevcoord = start
    visheight = grid[start[0]][start[1]][0]
    seen = 0

    while visheight < 9:
        newcoord = (prevcoord[0]+direction[0],prevcoord[1]+direction[1])
        new = grid[newcoord[0]][newcoord[1]]
        #if next point is on the edge, return
        if newcoord[0] == 0 or newcoord[0] == GRIDSIZE -1 or newcoord[1] == 0 or newcoord[1] == GRIDSIZE-1:
            return seen + 1
        # if next point is taller OR EQUAL TO than previous visheight,view is blocked, return seen (+1 counting this one)
        if new[0] >= visheight:
            return seen + 1
        #if next point is smaller, +1 tree seen
        seen += 1
        prevcoord = newcoord
    return seen

scores = []
for row in range(1,GRIDSIZE - 1):
    for col in range(1,GRIDSIZE - 1):
        right = look2(grid,(row,col),(1,0))
        left = look2(grid,(row,col),(-1,0))
        up = look2(grid,(row,col),(0,1))
        down = look2(grid,(row,col),(0,-1))
        scores.append(right*left*up*down)

print("PART 2:,", max(scores))
