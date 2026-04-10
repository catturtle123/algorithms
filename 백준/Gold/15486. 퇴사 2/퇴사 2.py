# N + 1 퇴사를 위해 N일 동안 최대한 많은 상담
# T는 상담이 걸리는 시간, 퇴사 이후의 시간까지 잡아먹는 일은 불가능
# P는 보수
# 최대 이익을 구하라
# 입력, N, T, P


import sys
input = sys.stdin.readline

n = int(input())
nlist = []
for _ in range(n):
    a, b = map(int, input().split())
    nlist.append((a, b))

# 각 날의 최대 값이 최대값이 될 수 있다
nlist.insert(0, 0)
dp = [0] * 1_500_051
temp = 0
for i in range(1, len(nlist)):
    time, value = nlist[i]
    temp = max(temp, dp[i])
    dp[i + time] = max(dp[i + time], temp + value)

print(max(dp[:n+2]))