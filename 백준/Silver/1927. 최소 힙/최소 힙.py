import sys, heapq
input = sys.stdin.readline

n = int(input())
nlist = []
heapq.heapify(nlist)

for i in range(n):
    m = int(input())

    if m == 0:
        if len(nlist) == 0:
            print(0)
        else:
            print(heapq.heappop(nlist))
    else:
        heapq.heappush(nlist, m)