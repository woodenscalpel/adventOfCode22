rawpackets = open("input.txt").read().split("\n\n")

packets = []
for packet in rawpackets:
    packets.append([eval(x)for x in packet.split("\n")[0:2]])

def ordercheck(leftlist,rightlist):
    #print("COMPARING ",leftlist,rightlist)

    leftlen = len(leftlist)
    rightlen = len(rightlist)
    minlen = min(leftlen,rightlen)

    for i in range(minlen):
        left = leftlist[i]
        right = rightlist[i]
        #print("checking ",left,right)
        if left == right:
            pass
        elif type(left) == int and type(right) == int:
            #print("RETURNING", left < right)
            return left < right
        else:
            if type(left) == int:
                left = [left]
            if type(right) == int:
                right = [right]
            recurse = ordercheck(left,right)
            if recurse != -1:
                return recurse
    if leftlen == rightlen:
        return -1
    return(leftlen < rightlen)



accum = []
part2packets = []
for packet in packets:
    left = packet[0]
    right = packet[1]
    part2packets.append(left)
    part2packets.append(right)
    accum.append(ordercheck(left,right))
silver = 0
#print(accum)
for idx,x in enumerate(accum):
    if x == True: silver += idx+1
print("silver:",silver)

#PART 2
def bubblepass(packets):
    swappedflag = False
    for i in range(len(packets)-1):
        if ordercheck(packets[i],packets[i+1]) == False:
            packets[i],packets[i+1] = packets[i+1],packets[i]
            swappedflag = True
    return swappedflag

part2packets.append([[2]])
part2packets.append([[6]])
done = True
while done == True:
    done = bubblepass(part2packets)

for idx,packet in enumerate(part2packets):
    if packet == [[2]]:
        p1 = idx+1
    if packet == [[6]]:
        p2 = idx+1
        print("gold",p1*p2)
