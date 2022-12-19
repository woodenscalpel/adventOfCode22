f = open("input.txt").readlines()
cubes =[tuple([int(x) for x in line.strip().split(',')]) for line in f]

print(cubes)

surfaceareas = 0

def neighbours(cube):
    x,y,z = cube
    return[(x,y,z+1),(x,y,z-1),(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z)]

accum = 0
for cube in cubes:
    airsides = 6
    for n in neighbours(cube):
        if n in cubes:
            airsides -= 1
    accum += airsides


#flood fill
start = {(-1,-1,-1)}

def flood(cubes,inputcubes):
    returnlist = set()
    for cube in cubes:
        for n in neighbours(cube):
            if n not in inputcubes:
                if n not in cubes:
                    x,y,z = n
                    if -2 < x and x < 23 and -2 < y and y < 23 and -2 < z and z < 23:
                        returnlist.add(n)
    returnlist.update(cubes)
    return returnlist

print(accum)

oldlen = -2
newlen = -1
while newlen != oldlen:
    start = flood(start,cubes)
    oldlen = newlen
    newlen = len(start)

accum = 0
for cube in cubes:
    for n in neighbours(cube):
        if n in start:
            accum += 1

print(accum)
