import sys
input = sys.stdin.readline

n = int(input())

tplist = []
for i in range(n):
    a, b = map(int, input().split())
    tplist.append((a, b))

dp = [0] * (n + 2)

for i in range(1, n + 1):
    if i + tplist[i - 1][0] > n + 1:
        continue

    dp[i + tplist[i - 1][0]] = max(max(dp[:i + 1])+ tplist[i - 1][1], dp[i + tplist[i - 1][0]])

print(max(dp))