import heapq
import sys
input = sys.stdin.readline

nlist = []

n = int(input())
cnt = 0
for _ in range(n):
    num = int(input())

    if num == 0:
        if cnt == 0:
            print(0)
        else:
            print(-(heapq.heappop(nlist)))
            cnt -= 1
    else:
        heapq.heappush(nlist, -num)
        cnt += 1