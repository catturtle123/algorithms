import heapq
import sys
input = sys.stdin.readline

nlist = []

n = int(input())
for _ in range(n):
    num = int(input())

    if num == 0:
        if not nlist:
            print(0)
        else:
            print(heapq.heappop(nlist)[1])
    else:
        if num < 0:
            heapq.heappush(nlist, (abs(num), num))
        else:
            heapq.heappush(nlist, (num, num))
    
