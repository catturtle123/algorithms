n, m, k = map(int, input().split(' '))

dp = [[1] * (m + 1) for _ in range(n + 1)]

dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

finish = False
if dp[n][m] < k:
    print(-1)
    finish = True

slist = []
while True:
    if m == 0 or n == 0:
        break
    
    if k <= dp[n - 1][m]:
        slist.append('a')
        n -= 1
    else:
        k -= dp[n - 1][m]
        slist.append('z')
        m -= 1

for i in range(n):
    slist.append("a")

for j in range(m):
    slist.append("z")

if not finish:
    for i in slist:
        print(i, end="")