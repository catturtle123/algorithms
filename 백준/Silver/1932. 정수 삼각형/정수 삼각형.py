import sys

input = sys.stdin.readline

n = int(input())

dp = [[0] * n for _ in range(n)]
for i in range(n):
    nlist = list(map(int, input().split()))
    for j in range(len(nlist)):
        dp[i][j] = nlist[j]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + dp[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1] + dp[i][j], dp[i - 1][j] + dp[i][j])


print(max(dp[n - 1]))