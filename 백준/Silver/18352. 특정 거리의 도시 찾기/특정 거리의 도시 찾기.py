import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split(" "))

g = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split(" "))
    g[a].append(b)

def bfs(g, start, visited):
    queue = deque([start])
    visited[start] = True

    count = 0
    length_list[start] = count

    while queue:
        count += 1
        q = queue.popleft()
        
        for i in g[q]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                length_list[i] = length_list[q] + 1


visited = [False] * (N + 1)
length_list = [1_000_000_2] * (N + 1)

bfs(g, X, visited)

final = False
for i in range(1, len(length_list)):
    if length_list[i] == K:
        print(i)
        final = True

if not final:
    print(-1)