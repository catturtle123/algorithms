dp = [0] * 5001
n = int(input())

dp[3] = 1
dp[5] = 1
for i in range(6, n + 1):
    d_5, d_3 = dp[i - 5], dp[i - 3]
    if d_5 != 0 and d_3 != 0:
        dp[i] = min(dp[i - 5], dp[i - 3]) + 1
    elif d_5 == 0 and d_3 != 0:
        dp[i] = d_3 + 1
    elif d_5 != 0 and d_3 == 0:
        dp[i] = d_5 + 1

if dp[n] == 0:
    print(-1)
else:
    print(dp[n])