# 계단을 오르면 점수를 얻음
# 규칙
# 1. 1, 2 계단씩 오를 수 있다.
# 2. 연속된 3계단을 밟아서는 안된다
# 3. 마지막 계단은 무조건 밟아야한다.
# 최댓값을 구하여라

import sys
input = sys.stdin.readline

n = int(input())
stairs = []
for _ in range(n):
    n2 = int(input())
    stairs.append(n2)

# i - 1, i - 2 중 더 큰 값을 나와 더한다
# 10 20 15 25

# 10, 30, 35, 60 or 55 or 

dp = [0] * n

if n < 3:
    if n == 1:
        print(stairs[0])
    elif n == 2:
        print(stairs[0] + stairs[1])
    else:
        print(stairs[2] + max(stairs[0], stairs[1]))
else:
    dp[0] = stairs[0]
    dp[1] = (stairs[1], dp[0] + stairs[1])
    dp[2] = (dp[0] + stairs[2], dp[1][0] + stairs[2])

    # 직전 값은 그 이이전의 값에서 올라온거
    # 직직전의 값은 모든 값

    for i in range(3, n):
        dp[i] = (max(dp[i - 2]) + stairs[i], dp[i - 1][0] + stairs[i])

    print(max(dp[n - 1]))