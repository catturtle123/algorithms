# 순열 사이클
# 순열 사이클의 갯수를 구하는 문제
# 2 x n 배열이 있을 때 위 숫자가 밑의 노드로 화살표가 이어지는 형식

import sys
from collections import deque
input = sys.stdin.readline

def bfs(cycles, start):
    global result

    if visited[start]:
        return

    queue = deque([start])
    result += 1

    while queue:
        num = queue.popleft()

        for i in cycles[num]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

n = int(input())

for _ in range(n):
    n2 = int(input())
    numbers = list(map(int, input().split()))

    cycles = [[] for _ in range(n2 + 1)]
    for i in range(1, n2 + 1):
        cycles[i].append(numbers[i - 1])
    
    result = 0
    visited = [False] * (n2 + 1)
    
    for i in range(1, n2 + 1):
        bfs(cycles, i)
    
    print(result)