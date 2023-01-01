import sys

n = int(input())

nlist = []

for i in range(10000):
    nlist.append(0)


for i in range(n):
    num = int(sys.stdin.readline().strip())
    nlist[num-1] += 1

count = 1
for i in nlist:
    for j in range(i):
        print(count)
    count += 1
        
    
