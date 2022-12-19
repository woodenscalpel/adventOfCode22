import copy
TIMELEFT = 30

class node:
    def __init__(self,_id,flowrate,connections):
        self.id = _id
        self.flowrate = flowrate
        self.connections = connections
        
nodes = {}
for line in open("input.txt"):
    name = line.strip().split(" ")[1]
    flow = int(line.strip().split(" ")[4].split("=")[1].strip(";"))
    connections = [connection.strip(",") for connection in line.strip().split(" ")[9:]]
    nodes[name] = [flow,connections,False]

paths = [['AA',30,0,set()]]
#A path has current node,time left, released pressure so far, and list of nodes it has opened
#Step function takes a path, and spawns a list of N paths for each choice it can make

def addedpressure(opened):
    accum = 0
    for node in opened:
        accum += nodes[node][0]
    return accum

def traversepath(path):
    pathname,time,pressure,opened = path
    newpaths = []
    #if time left is 0, do nothing
    if time <= 0:
        return path
    #go to connected nodes
    for connection in nodes[pathname][1]:
        newpaths.append([connection,time-1,pressure,opened])
    #Try to open valve
    if (pathname not in opened) and nodes[pathname] != 0:
        newopened = copy.deepcopy(opened)
        newopened.add(pathname)
        #total pressure from valve = (time-1)*flow
        pressure += (time-1)*nodes[pathname][0]
        newpaths.append([pathname,time-1,pressure,newopened])

    return newpaths

def prune(paths,maxsteam):
    STEAMPRUNETHRESH = maxsteam - 150
    newpaths = [paths[0]]
    for oldpath in paths:
        #not enough steam
        if oldpath[2] > STEAMPRUNETHRESH:

            dupe = False
            for newpath in newpaths:
                if oldpath == newpath:
                    dupe = True
                #If item in same node with same connections and with less steam, discard
                    if (oldpath[3].issubset(newpath[3])):
                        if oldpath[2] <= newpath[2]:
                            dupe = True
            if dupe == False:
                newpaths.append(oldpath)
    return newpaths


maxsteam = 0
for i in range(30):
    newpaths = []
    for path in paths:
        newpaths.extend(traversepath(path))
    paths = prune(newpaths,maxsteam)
    print(i)
    print(sorted(paths))
    print("L",len(paths))
    steam = [path[2] for path in paths]
    maxsteam = max(steam)
steam = [path[2] for path in paths]
print(max(steam))

