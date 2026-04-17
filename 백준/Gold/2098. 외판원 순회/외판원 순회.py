# 한 도시에서 출발해 N개의 도시를 거쳐 돌아오는 것
# 한번 갔던 도시를 다시 갈 수는 없음

import sys
input = sys.stdin.readline

n = int(input())
cost_list = []
for _ in range(n):
    temp = list(map(int, input().split()))
    cost_list.append(temp)

INF = sys.maxsize
dp = [[-1] * (1 << n) for _ in range(n)]

def dfs(now, visited):
    # 모든 곳 방문 완료
    if visited == (1 << n) - 1:
        if cost_list[now][0] == 0:
            return INF
        return cost_list[now][0]

    # 이미 방문
    if dp[now][visited] != -1:
        return dp[now][visited]

    # 초기 값 설정
    dp[now][visited] = INF

    # 순회
    for i in range(n):
        if visited & (1 << i):
            continue

        if cost_list[now][i] == 0:
            continue

        cost = cost_list[now][i] + dfs(i, visited | (1 << i))
        dp[now][visited] = min(dp[now][visited], cost)
    
    return dp[now][visited]

print(dfs(0, 1))