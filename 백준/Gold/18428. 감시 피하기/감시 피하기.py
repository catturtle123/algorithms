import sys, copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n = int(input())

maps = []
for i in range(n):
    maps.append(list(map(str, input().split())))
    
Xlist = []
Tlist = []
Slist = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == "X":
            Xlist.append((i, j))
        elif maps[i][j] == "T":
            Tlist.append((i, j))
        elif maps[i][j] == "S":
            Slist.append((i, j))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for comb in combinations(Xlist, 3):
    new_maps = copy.deepcopy(maps)

    for i in comb:
        new_maps[i[0]][i[1]] = "O"
    
    # 되는 지 확인
    is_avoid = True
    for t_pos in Tlist:
        dir = 0
        y = t_pos[0]
        x = t_pos[1]
        
        while True:
            ny, nx = dy[dir] + y, dx[dir] + x

            if 0 <= ny < n and 0 <= nx < n:
                if new_maps[ny][nx] == "O":
                    dir += 1
                    y = t_pos[0]
                    x = t_pos[1]
                    
                    if dir == 4:
                        break

                elif new_maps[ny][nx] == "X" or new_maps[ny][nx] == "T":
                    y = ny
                    x = nx
                elif new_maps[ny][nx] == "S":
                    is_avoid = False
                    break
            else:
                dir += 1
                y = t_pos[0]
                x = t_pos[1]  

                if dir == 4:
                    break
        
        if not is_avoid:
            break

    if is_avoid:
        print("YES")
        break

if not is_avoid:
    print("NO")                   