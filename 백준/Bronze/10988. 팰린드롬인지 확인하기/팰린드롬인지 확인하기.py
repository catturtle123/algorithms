n = input()

nlist = [i for i in n]

o = 0
for i in range(len(nlist)):
    if nlist[i] != nlist[-1-i]:
        print(0)
        o = 1
        break
    

if o != 1:
    print(1)