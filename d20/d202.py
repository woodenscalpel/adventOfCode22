def newMod(a,b):
    res = a%b
    return res if not res else res-b if a<0 else res

f = open("input.txt").readlines()

key = 811589153

nums = [[int(x)*key, idx] for idx,x in enumerate(f)]

def mix(numlist):
    llen = len(numlist)
    for i in range(llen):
        for idx, n in enumerate(numlist):
            if n[1] ==i:
                nextidx = idx
                nextn = n[0]
                nextmov = n[0]
                origorder = n[1]
                break
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

        newitem = [nextn,origorder]
        numlist.insert(newidx,newitem)
        if newidx > idx:
            del numlist[idx]
        else:
            del numlist[idx+1]
    return numlist

print(nums)
for i in range(10):
    nums = mix(nums)
    print(nums)
for idx,i in enumerate(nums):
    if i[0] == 0:
        zidx = idx
#print(len(nums))
llen = len(nums)
print(nums[(zidx+1000)%llen][0] + nums[(zidx+2000) %llen][0] +nums[(zidx+3000) %llen][0])
