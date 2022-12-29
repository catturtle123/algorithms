a,b = map(int,input().split())


nlist = []
for i in range(1,a+1):
    if a % i == 0:
        if b % i == 0:
          nlist.append(i)


print(nlist[-1])  
a = a/nlist[-1]
b = b/nlist[-1]
print(int(a*b*nlist[-1]))