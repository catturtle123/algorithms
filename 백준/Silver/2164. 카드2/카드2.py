from collections import deque

n = int(input())

nlist = [i for i in range(1, n + 1)]
nqueue = deque(nlist)

while len(nqueue) > 1:
    nqueue.popleft()
    q = nqueue.popleft()
    nqueue.append(q)

print(nqueue[0])