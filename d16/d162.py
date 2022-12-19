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

paths = [[['AA','AA'],26,0,set()]]
#A path has [current node, elephant node],time left, released pressure so far, and list of nodes it has opened
#Step function takes a path, and spawns a list of N paths for each choice it can make

def addedpressure(opened):
    accum = 0
    for node in opened:
        accum += nodes[node][0]
    return accum

def traversepath(path):
    names,time,pressure,opened = path
    mynode,elenode = names
    newpaths = []
    #if time left is 0, do nothing
    if time <= 0:
        return path

    #I go to connected nodes
    for connection in nodes[mynode][1]:

        #Elephant goes to his nodes
        for connection2 in nodes[elenode][1]:
            newpaths.append([[connection,connection2],time-1,pressure,opened])

        #Or elephant tries to open his node
        if (elenode not in opened) and nodes[elenode] != 0:
            newopened = copy.deepcopy(opened)
            newopened.add(elenode)
            #total pressure from valve = (time-1)*flow
            newpressure = pressure + (time-1)*nodes[elenode][0]
            newpaths.append([[connection,elenode],time-1,newpressure,newopened])

    #Or I try to open my node
    if (mynode not in opened) and nodes[mynode] != 0:
        newopened = copy.deepcopy(opened)
        newopened.add(mynode)
        #total pressure from valve = (time-1)*flow
        newpressure = pressure + (time-1)*nodes[mynode][0]

        #Elephant goes to his nodes
        for connection2 in nodes[elenode][1]:
            newpaths.append([[mynode,connection2],time-1,newpressure,newopened])

        #Or elephant tries to open his node
        if (elenode not in opened) and nodes[elenode] != 0 and mynode != elenode:
            newopened2 = copy.deepcopy(newopened)
            newopened2.add(elenode)
            #total pressure from valve = (time-1)*flow
            newpressure2 = newpressure + (time-1)*nodes[elenode][0]
            newpaths.append([[mynode,elenode],time-1,newpressure2,newopened2])


        """
        newpaths.append([connection,time-1,pressure,opened])
    #Try to open valve
    if (pathname not in opened) and nodes[pathname] != 0:
        newopened = copy.deepcopy(opened)
        newopened.add(pathname)
        #total pressure from valve = (time-1)*flow
        pressure += (time-1)*nodes[pathname][0]
        newpaths.append([pathname,time-1,pressure,newopened])
        """

    return newpaths

def prune(paths,maxsteam):
    STEAMPRUNETHRESH = maxsteam - 200
    newpaths = [paths[0]]
    for oldpath in paths:
        #not enough steam
        if oldpath[2] > STEAMPRUNETHRESH:

            dupe = False
            for newpath in newpaths:
                if oldpath == newpath:
                    dupe = True
                #If item in same node[S] with same connections and with less steam, discard
                if oldpath[0] == newpath[0] or (oldpath[0][1] == newpath[0][0] and oldpath[0][0] == newpath[0][1]):
                    if (oldpath[3].issubset(newpath[3])):
                        if oldpath[2] <= newpath[2]:
                            dupe = True
            if dupe == False:
                newpaths.append(oldpath)
    return newpaths


maxsteam = 0
for i in range(26):
    newpaths = []
    for path in paths:
        newpaths.extend(traversepath(path))
    paths = prune(newpaths,maxsteam)
    print(i)
    #print(sorted(paths))
    print("L",len(paths))
    steam = [path[2] for path in paths]
    maxsteam = max(steam)
    print("STE",maxsteam)
steam = [path[2] for path in paths]
print(max(steam))

