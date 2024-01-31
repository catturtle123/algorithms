n = int(input())


dp = []

for i in range(1516):
    dp.append(0)

dp[0] = 0
dp[1] = 2
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = dp[i - 2] * 2 + dp[i - 1]

print((pow(2, n) - dp[n]) % 1_000_000_007)

