import sys, bisect
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))

m = int(input())
mlist = list(map(int, input().split()))

nlist.sort()
for i in mlist:
    a = bisect.bisect_left(nlist, i)

    b = bisect.bisect_right(nlist, i)

    print(b - a, end=" ")