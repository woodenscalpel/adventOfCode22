import sys
import copy
sys.setrecursionlimit(100000) #lol

hmap = [[ord(x) - ord('a') for x in line.strip()] for line in open("input.txt").readlines()]
ncols = len(hmap)
nrows = len(hmap[0])

start = ord('S') - ord('a')
end = ord('E') - ord('a')

for idxi, i in enumerate(hmap):
    for idxj, j in enumerate(i):
        if j == start:
            startidx = (idxi,idxj)

# [distance, visited]
distances = [[[9999999999,False] for x in range(nrows)] for y in range(ncols)]
distances[startidx[0]][startidx[1]] = [0,True] #start node

def neighbours(idx):
    #neighbours and also bounds checking
    neigh = [(idx[0]+1,idx[1]),(idx[0]-1,idx[1]),(idx[0],idx[1]+1),(idx[0],idx[1]-1)]
    neighbounded = []
    for n in neigh:
        if 0 <= n[0] and n[0] <= ncols-1 and 0 <= n[1] and n[1] <= nrows-1:
            neighbounded.append(n)
    return(neighbounded)

def badsort(d):
    #should be a one-liner listcomp
    minval = 999999
    index = None
    for idx,row in enumerate(d):
        for jdx,item in enumerate(row):
            if item[0] < minval and item[1] == False:
                minval = item[0]
                index = (idx,jdx)
    return index

#djik to find distances
def djikstep(hmap,dist,currentnodeidx,ENDIDX):
    idx = currentnodeidx[0]
    jdx = currentnodeidx[1]
    h = hmap[idx][jdx]
    if h == start: h = 0
    currdist = dist[idx][jdx][0]

    #Can move to node if nh <= h+1 (and algo hasnt visited yet)
    reachablenodes = []
    for nodeidx in neighbours(currentnodeidx):
        nh = hmap[nodeidx[0]][nodeidx[1]]
        if nh == end:
            ENDIDX = nodeidx
            nh = 26
        if nh <= h+1 and dist[nodeidx[0]][nodeidx[1]][1] == False:
            reachablenodes.append(nodeidx)

    #for node in reachable nodes, update distance
    for nodeidx in reachablenodes:
        nodedistance = 1 #PROBABLY CHANGE FOR PART 2
        if currdist + nodedistance < dist[nodeidx[0]][nodeidx[1]][0]:
            dist[nodeidx[0]][nodeidx[1]][0] = currdist + nodedistance

    nextnodeidx = badsort(dist)
    if nextnodeidx == None: return dist[ENDIDX[0]][ENDIDX[1]][0]

    dist[nextnodeidx[0]][nextnodeidx[1]][1] = True
    return djikstep(hmap,dist,nextnodeidx,ENDIDX)


aspots = []
for idx,row in enumerate(hmap):
    for jdx,col in enumerate(row):
        if col == 0:
            aspots.append((idx,jdx))

distance = copy.deepcopy(distances) 
endidx = djikstep(hmap,distance,startidx,None)
distlist = []
for start in aspots:
    distance = copy.deepcopy(distances) 
    distance[start[0]][start[1]] = [0,True] #start node
    endidx = djikstep(hmap,distance,start,(0,0))
    distlist.append(endidx)
print(sorted(distlist)[0])

