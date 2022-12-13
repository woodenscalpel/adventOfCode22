f = open("input.txt").readline()
for i in range(10000): 
    if len(set(f[i:i+14])) == 14: print(i+14)

