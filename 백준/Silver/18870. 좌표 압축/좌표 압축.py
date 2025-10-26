import sys
import bisect
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))

nlist2 = sorted(set(nlist))

result = {}
for i in nlist2:
    a = bisect.bisect_left(nlist2, i)
    
    result[i] = a

for i in nlist:
    print(result[i], end=" ")