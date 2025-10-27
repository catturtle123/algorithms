import sys
from collections import deque
input = sys.stdin.readline

INF = sys.maxsize

def bfs(start):
    queue = deque([start])

    while queue:
        pos, length = queue.popleft()

        if pos == k:
            break

        if 0 <= pos + 1 <= 100_000:
            if dp[pos + 1] == INF:
                dp[pos + 1] = min(dp[pos + 1], length + 1)
                queue.append((pos + 1, dp[pos + 1]))
        
        if 0 <= pos - 1 <= 100_000:
            if dp[pos - 1] == INF:
                dp[pos - 1] = min(dp[pos - 1], length + 1)
                queue.append((pos - 1, dp[pos - 1]))
        
        if 0 <= 2 * pos <= 100_000:
            if dp[2 * pos] == INF:
                dp[2 * pos] = min(dp[pos * 2], length + 1)
                queue.append((2 * pos, dp[2 * pos]))

n, k = map(int, input().split())

dp = [INF] * (100_001)
dp[n] = 0

bfs((n, 0))

print(dp[k])