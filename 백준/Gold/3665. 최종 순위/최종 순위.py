import sys, copy
from collections import deque
input = sys.stdin.readline

t = int(input()) # 테스트 케이스 수

for i in range(t):
    n = int(input())
    in_degree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    nlist = list(map(int, input().split()))

    for j in range(n):
        for o in range(j + 1, len(nlist)):
            graph[nlist[j]].append(nlist[o])
            in_degree[nlist[o]] += 1
    
    m = int(input())
    for j in range(m):
        a, b = map(int, input().split())

        if b in graph[a]:
            graph[a].remove(b)
            in_degree[b] -= 1
            graph[b].append(a)
            in_degree[a] += 1
        elif a in graph[b]:
            graph[b].remove(a)
            in_degree[a] -= 1
            graph[a].append(b)
            in_degree[b] += 1
        
    q = deque([])
    result = []
    for j in range(len(nlist)):
        if in_degree[nlist[j]] == 0:
            q.append(nlist[j])
    
    count = 0
    while q:
        if len(q) >= 2:
            print("?")
        now = q.popleft()
        result.append(now)
        count += 1           
            

        for j in graph[now]:
            in_degree[j] -= 1
            if in_degree[j] == 0:
                q.append(j)
    
    if count != n:
        print("IMPOSSIBLE")
    else:
        for j in result:
            print(j, end=" ")
        print()