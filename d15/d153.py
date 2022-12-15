f = open("input.txt")

#PARSE

sensors = []
for line in f:
    words = line.strip().split(" ")
    sx = int(words[2].split("=")[1].strip(","))
    sy = int(words[3].split("=")[1].strip(":"))
    bx = int(words[-2].split("=")[1].strip(","))
    by = int(words[-1].split("=")[1])
    sensors.append([[sx,sy],[bx,by]])

for targety in range(0,4000000):

    #FOR EACH SENSOR, find interval of points where beacon CANT be

    intervals = []
    for sensor in sensors:
        dy = sensor[0][1] - sensor[1][1] #diff from sensor to beacon
        dx = sensor[0][0] - sensor[1][0] #diff from sensor to beacon
        sensorwidth = abs(dx) + abs(dy)
        sensorminx = sensor[0][0] - sensorwidth
        sensormaxx = sensor[0][0] + sensorwidth

        dt = sensor[0][1] - targety #diff from sensor to target

        targetwidth = sensorwidth - abs(dt)
        targetminx = sensor[0][0] - targetwidth
        targetmaxx = sensor[0][0] + targetwidth
        if targetmaxx > targetminx:
            intervals.append([targetminx,targetmaxx])


    #Merge these intervals into minimal set

    sortedintervals = sorted(intervals)
    #print(sortedintervals)
    newintervals = []
    newintervals.append(sortedintervals[0])
    for i in range(1,len(intervals)):
        if sortedintervals[i][0] <= newintervals[-1][1]+1:
            newintervals[-1][1] = max(sortedintervals[i][1],newintervals[-1][1])
        else:
            newintervals.append(sortedintervals[i])
    #print(newintervals)

    #If there is a break in the intervals within our target reigon, we found the point

    intervalfound = False
    for interval in newintervals:
        if interval[0] <= 0 and interval[1] >= 4000000:
        #if interval[0] <= 0 and interval[1] >= 20:
            intervalfound = True
    if intervalfound == False:
        print("FOUND",newintervals,targety)
        print((newintervals[0][1]+1)*4000000+targety)
