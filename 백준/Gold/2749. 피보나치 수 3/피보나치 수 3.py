import sys
input = sys.stdin.readline

n = int(input())
n %= 1_500_000

dp = [0] * (n + 1)

if n >= 1:
    dp[1] = 1

for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1_000_000

print(dp[n])