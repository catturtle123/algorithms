import sys
from collections import deque
import heapq
input = sys.stdin.readline

n = int(input())

nlist = []
for i in range(n):
    a = int(input())
    nlist.append(a)

heapq.heapify(nlist)

result = []
sums = 0
while len(nlist) > 1:
    q1 = heapq.heappop(nlist)
    q2 = heapq.heappop(nlist)
    
    heapq.heappush(nlist, q1 + q2)
    result.append(q1 + q2)

print(sum(result))