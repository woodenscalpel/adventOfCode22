import math
import copy
f = open("input.txt").readlines()

def maxscore(time,current,mine):
    accum = current
    while time != 0:
        accum += time
        time -= 1
    return accum

def computenextstate(nextstate,c,purchaseidx):
    #This function only exists to terminate nested loops with return statements because i mess up break and continue every time

    m,r,t = nextstate #unpack miners, resources, time
    #Wait until we can afford the next thing, return state after the timestep we buy it
    canafford = False
    if r[0] >= c[0] and r[1] >= c[1] and r[2] >= c[2]: 
        canafford = True
    while canafford == False:
        r = tuple(sum(x) for x in zip(m,r)) #generate for a step
        t -= 1
        if t <=0:
            return -1
        if r[0] >= c[0] and r[1] >= c[1] and r[2] >= c[2]: 
            canafford = True
    #We have enough money now. Compute state after purchase
    r = tuple(r - c for (r,c) in zip(r,c))

    r = tuple(sum(x) for x in zip(m,r)) #generate for a step
    t -= 1

    #yikes. I still want everything to be tuples so i can store the states in a set
    m = list(m)
    m[purchaseidx] += 1
    m = tuple(m)

    return((m,r,t))




def buystep(gamestate,costs,maxcosts):
    #branch state for each bot we can buy next
    nextstates = []
    for idx,c in enumerate(costs):
        #If we are generating enough to buy the most expensive
        #thing every turn, we dont need to build any more bots
        if gamestate[0][idx] >= maxcosts[idx]:
            continue

        nextstate = copy.deepcopy(gamestate) # no funny business with allocating python lists
        nextstate = computenextstate(nextstate,c,idx)
        if nextstate != -1:
            nextstates.append(nextstate)
    #finally, add the state if we dont make any more miners, just generate the rest of the geodes before time is out
    m,r,t = gamestate #unpack miners, resources, time
    while t > 0:
        r = tuple(sum(x) for x in zip(m,r)) #generate for a step
        t -= 1
    nextstates.append((m,r,t))
    return(nextstates)


MAXG_ARRAY = []
for blue in f:
    MAXG = 0 #Output
    #Parse out lines
    lines = blue.split(".")
    orecost = (int(lines[0].split(" ")[6]),0,0,0)
    claycost =(int(lines[1].split(" ")[5]),0,0,0)
    obbycost = (int(lines[2].split(" ")[5]),int(lines[2].split(" ")[8]),0,0)
    geodecost = (int(lines[3].split(" ")[5]),0,int(lines[3].split(" ")[8]),0)
    resourcecosts = (orecost,claycost,obbycost,geodecost)
    
    #get maximum cost of each item for pruning later
    maxorecost = max([r[0] for r in resourcecosts])
    maxclaycost = max([r[1] for r in resourcecosts])
    maxobbycost = max([r[2] for r in resourcecosts])
    maxgeodecost = 999 #Always make geodes
    maxcosts = (maxorecost,maxclaycost,maxobbycost,maxgeodecost)

    #inital state
    miners = (1,0,0,0)
    resources = (0,0,0,0)
    timeleft = 24
    gamestate = (miners,resources,timeleft)
    gamestates = set()
    gamestates.add(gamestate)

    while len(gamestates) > 0:
        print("NEXTSTEP")
        newstates = set()
        for state in gamestates:
            newstates.update(buystep(state,resourcecosts,maxcosts))

        gamestates = set()
        for state in newstates:
            if state[2] > 0:
                gamestates.add(state)
            else:
                if state[1][3] > MAXG:
                    MAXG = state[1][3]

    print(MAXG)
    MAXG_ARRAY.append(MAXG)
accum = 0
for idx,item in enumerate(MAXG_ARRAY):
    accum += (idx+1)*item
print(accum)
