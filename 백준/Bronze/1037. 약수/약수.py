n = int(input())
nlist = list(map(int,input().split()))

nlist.sort()

print(nlist[0]*nlist[-1])