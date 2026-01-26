n = int(input())

nlist1 = list(map(int, input().split()))
nlist2 = list(map(int, input().split()))

sums = sum(nlist1)
print(sums)

for i in range(len(nlist2)):
    if nlist2[i] == 1:
        sums -= nlist1[i]
        
print(sums)