import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split(" ")))

if n % 2 == 0:
    target = n // 2
else:
    target = (n + 1) // 2

nlist.sort()

print(nlist[target - 1])