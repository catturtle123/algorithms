import sys
input = sys.stdin.readline

n = int(input())
nlist = [0] * (n + 1)


if n >= 3:
    nlist[1] = 1
    nlist[2] = 1
    for i in range(3, n + 1):
        nlist[i] = nlist[i - 1] + nlist[i - 2]
    print(nlist[n])
else:
    print(1)