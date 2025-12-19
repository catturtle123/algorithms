import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

nlist = []
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(nlist, (a, b))

klist = []
for _ in range(k):
    a = int(input())
    klist.append(a)

klist.sort()

result = 0
temp = []
for bag in klist:
    while nlist and nlist[0][0] <= bag:
        m, v = heapq.heappop(nlist)
        heapq.heappush(temp, -v)

    if temp:
        result += -heapq.heappop(temp)

print(result)
