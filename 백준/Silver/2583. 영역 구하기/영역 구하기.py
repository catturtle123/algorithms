# 1초, m,n,k 100 이하 n^2도 가능
# M, N 크기의 모눈 종이, K개의 직사각형을 그림
# 내부에 그려진 직사각형을 제외한 모양의 크기 -> 한 칸당 넓이 1로 간주
# 몇개로 분리, 분리된 각 영역이 얼마인지
# 왼쪽 아래의 꼭지점, 오른쪽 위의 꼭지점
# 그래프 -> 넓이 우선 탐색, 깊이 우선 탐색 -> 1로 색칠하고 1이 아니라면 dfs -> 0일 시 다시 시작 -> 갯수와 넓이 가능

dy = [1, -1, 0, 0]
dx = [0, 0, 1, - 1]

import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())
nlist = [[0] * n for _ in range(m)] # n x m

klist = [] # x1, y1, x2, y2
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split()) 
    
    for i in range(y1, y2):
        for j in range(x1, x2):
            nlist[i][j] = 1

count = 0
result_list = []
queue = deque([])
for i in range(m):
    for j in range(n):
        if nlist[i][j] == 0:
            count += 1
            result = 0
            queue.append((i, j))

            nlist[i][j] = 1
            result += 1

            while queue:
                y, x = queue.pop()

                for dir in range(4):
                    ny = y + dy[dir]
                    nx = x + dx[dir]
                    
                    if 0 <= ny < m and 0 <= nx < n:
                        if nlist[ny][nx] == 0:
                            nlist[ny][nx] = 1
                            result += 1
                            queue.append((ny, nx))
            
            result_list.append(result)
                            
print(count)


result_list.sort()
for i in result_list:
    print(i, end=" ")