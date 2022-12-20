def newMod(a,b):
    res = a%b
    return res if not res else res-b if a<0 else res

f = open("input.txt").readlines()

nums = [[int(x), int(x)] for x in f]

def movenextnumber(numlist):
    llen = len(numlist)
    done = True
    for idx, n in enumerate(numlist):
        if n[1] !=0:
            nextidx = idx
            nextn = n[0]
            nextmov = n[1]
            done = False
            break
    if done == True:
        return [numlist,True]
    #print(nextn,nextidx,nextmov)
    #print(nextidx,nextmov,newMod(nextidx+nextmov,llen-1))
    #newidx = nextidx + newMod(nextmov,llen-1)+1
    newidx = newMod(nextidx +nextmov,llen-1)
    if newMod(nextidx +nextmov,llen-1) == 0: newidx = 0
    #print(newidx)
    if newidx < 0: newidx = llen + newidx - 1
    if newidx > llen: newidx = newidx - llen -1
    if newidx > idx: newidx +=1
    #print(newidx)

    newitem = [nextn,0]
    numlist.insert(newidx,newitem)
    if newidx > idx:
        del numlist[idx]
    else:
        del numlist[idx+1]
    return [numlist,False]

done = False
while done == False:
    [nums,done] = movenextnumber(nums)
    #print(nums)
zidx = nums.index([0,0])
print(nums)
#print(len(nums))
print(zidx)
llen = len(nums)
print((zidx+1000) % llen)
print(nums[(zidx+1000) %llen][0])
print(nums[(zidx+2000)%llen][0])
print(nums[(zidx+3000)%llen][0])
print(nums[(zidx+1000)%llen][0] + nums[(zidx+2000) %llen][0] +nums[(zidx+3000) %llen][0])
