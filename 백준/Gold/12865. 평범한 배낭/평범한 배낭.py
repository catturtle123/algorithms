import sys
input = sys.stdin.readline

n, k = map(int, input().split())
wvlist = []

for i in range(n):
    w, v = map(int, input().split())
    wvlist.append((w, v))

wvlist.sort()

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w, v = wvlist[i - 1][0], wvlist[i - 1][1]
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

result = 0
for i in range(n + 1):
    result = max(dp[i][k], result)

print(result)