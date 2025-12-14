import sys
from collections import deque
input = sys.stdin.readline

def topology():
    queue = deque([])

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = value[i]
    
    while queue:
        node = queue.popleft()

        for i in graph[node]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[node] + value[i])
            if indegree[i] == 0:
                queue.append(i)
                

t = int(input())
for _ in range(t):
    n, k = map(int, input().split()) # 건물의 개수, 건물간 순서 규칙
    
    dp = [0] * (n + 1)
    value = list(map(int, input().split()))
    value.insert(0, 0)
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for i in range(k):
        a, b = map(int, input().split())
        indegree[b] += 1
        graph[a].append(b)
    
    target = int(input())
    topology()
    
    # 그전 노드들 중 가장 큰 노드 가져오기
    print(dp[target])