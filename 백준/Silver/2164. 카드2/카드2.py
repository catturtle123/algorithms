from collections import deque

n = int(input())

nlist = list(range(1,n+1))
dequeData = deque(nlist)

while len(dequeData) != 1:
    dequeData.popleft()
    dequeData.insert(len(dequeData),dequeData[0])
    dequeData.popleft()


print(dequeData[0])