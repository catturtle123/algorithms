import sys
from copy import deepcopy
input = sys.stdin.readline

# 방향
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]

def move_fish(maps):
    for i in range(1, 17):
        found = False
        for y in range(4):
            for x in range(4):
                if maps[y][x][0] == i:
                    direct = maps[y][x][1]
                    for _ in range(8):
                        ny, nx = y + dy[direct], x + dx[direct]
                        # 이동 가능 칸
                        if 0 <= ny < 4 and 0 <= nx < 4 and maps[ny][nx][0] != 17:
                            # swap
                            maps[y][x][1] = direct
                            maps[y][x], maps[ny][nx] = maps[ny][nx], maps[y][x]
                            found = True
                            break
                        direct = direct + 1 if direct < 8 else 1
                    if found:
                        break
            if found:
                break

# 입력 처리
maps = []
for _ in range(4):
    a, b, c, d, e, f, g, h = map(int, input().split())
    maps.append([[a, b], [c, d], [e, f], [g, h]])

# 상어 시작
result = 0
first_fish_num, first_fish_dir = maps[0][0]
result += first_fish_num
maps[0][0] = [17, first_fish_dir]  # 상어 배치

max_score = 0

def dfs(board, shark_y, shark_x, shark_dir, total):
    global max_score
    max_score = max(max_score, total)

    new_map = deepcopy(board)
    move_fish(new_map)

    for step in range(1, 4):
        ny, nx = shark_y + dy[shark_dir] * step, shark_x + dx[shark_dir] * step

        if not (0 <= ny < 4 and 0 <= nx < 4):
            break
        if new_map[ny][nx][0] == 0:
            continue

        temp_map = deepcopy(new_map)
        fish_num, fish_dir = temp_map[ny][nx]
        temp_map[shark_y][shark_x] = [0, 0]
        temp_map[ny][nx] = [17, fish_dir]
        dfs(temp_map, ny, nx, fish_dir, total + fish_num)

dfs(maps, 0, 0, maps[0][0][1], result)
print(max_score)
