import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nlist = []
for i in range(1, m + 1):
    a, b = map(int, input().split())
    nlist.append((a, i))
    nlist.append((b, i))

nlist.sort()
count = 0
while True:
    count += 1
    
    q = nlist.pop(0)

    if count == n:
        print(q[1])
        break

    nlist.append(q)