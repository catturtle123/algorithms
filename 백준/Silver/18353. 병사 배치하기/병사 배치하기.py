import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))

nlist.insert(0, 0)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    temp = []
    for j in range(i):
        if nlist[i] < nlist[j]:
            temp.append(dp[j])
    
    if len(temp) == 0:
        temp.append(0)

    dp[i] = max(temp) + 1

print(n - max(dp))