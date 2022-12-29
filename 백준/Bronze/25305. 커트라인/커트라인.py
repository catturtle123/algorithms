a,b = map(int,input().split())

nlist = list(map(int,input().split()))

nlist.sort()
nlist.reverse()

print(nlist[b-1])