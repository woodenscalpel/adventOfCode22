f = open("input.txt")

sensors = []
for line in f:
    words = line.strip().split(" ")
    sx = int(words[2].split("=")[1].strip(","))
    sy = int(words[3].split("=")[1].strip(":"))
    bx = int(words[-2].split("=")[1].strip(","))
    by = int(words[-1].split("=")[1])
    sensors.append([[sx,sy],[bx,by]])

targety = 2000000

intervals = []

for sensor in sensors:
    dy = sensor[0][1] - sensor[1][1] #diff from sensor to beacon
    dx = sensor[0][0] - sensor[1][0] #diff from sensor to beacon
    sensorwidth = abs(dx) + abs(dy)
    sensorminx = sensor[0][0] - sensorwidth
    sensormaxx = sensor[0][0] + sensorwidth

    dt = sensor[0][1] - targety #diff from sensor to target
    print(dt)
    print(sensorwidth)

    targetwidth = sensorwidth - abs(dt)
    targetminx = sensor[0][0] - targetwidth
    targetmaxx = sensor[0][0] + targetwidth
    intervals.append([targetminx,targetmaxx])

print(intervals)

xcoords = set()
for interval in intervals:
    if interval[1] > interval[0]:
        for i in range(interval[0],interval[1]):
            xcoords.add(i)
print(len(xcoords))
