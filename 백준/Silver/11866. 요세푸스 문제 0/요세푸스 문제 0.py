import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

nlist = []
for i in range(1, n + 1):
    nlist.append(i)

count = 0

queue = deque(nlist)

result = []
while queue:
    count += 1

    q = queue.popleft()

    if count % k == 0:
        result.append(q)
    else:
        queue.append(q)

print("<",end="")
for i in result:
    if i == result[-1]:
        print(str(i) + ">")
        break
    print(str(i) + ", ", end="")