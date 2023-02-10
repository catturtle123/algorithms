n,m = map(int,input().split())
nlist = list(map(int,input().split()))

result = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if nlist[i] + nlist[j] + nlist[k] > m:
                continue
            else:
                result = max(result,nlist[i] + nlist[j] + nlist[k])


print(result)