n = int(input())

nlist = []
for i in range(n):
    num = int(input())
    if num == 0:
        nlist.pop()
    else: 
        nlist.append(num)

sum=0
if len(nlist) == 0:
    print(0)
else:
    for i in nlist:
        sum += i
    print(sum)