import sys, copy
input = sys.stdin.readline

r, c, t = map(int, input().split()) # y, x, 시간
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
real_map = []
for i in range(r):
    real_map.append(list(map(int, input().split())))

air_r_1 = 0
air_c_1 = 0
air_r_2 = 0
air_c_2 = 0
for i in range(r):
    if real_map[i][0] == -1:
        air_r_1 = i
        air_c_1 = 0
        air_r_2 = i + 1
        air_c_2 = 0
        break

for time in range(t):
    new_map = [[0] * c for _ in range(r)]
    
    # 미세먼지 확산
    for y in range(r):
        for x in range(c):
            if real_map[y][x] > 0:

                temp = 0
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < r and 0 <= nx < c and real_map[ny][nx] != -1:
                        new_map[ny][nx] += real_map[y][x] // 5
                        temp += (real_map[y][x] // 5)
                 
                new_map[y][x] += (real_map[y][x] - temp)    

    # 미세먼지 이동
    new_new_map = copy.deepcopy(new_map)
    # 위쪽
    for x in range(c - 2, -1, -1):
        new_new_map[air_r_1][x + 1] = new_map[air_r_1][x]
    
    for y in range(0, air_r_1):
        new_new_map[y][c - 1] = new_map[y + 1][c - 1]

    for x in range(0, c - 1):
        new_new_map[0][x] = new_map[0][x + 1]

    for y in range(air_r_1 - 2, -1, -1):
        new_new_map[y + 1][0] = new_map[y][0]

    # 아래
    for x in range(c - 2, -1, -1):
        new_new_map[air_r_2][x + 1] = new_map[air_r_2][x]

    for y in range(r - 2, air_r_2 - 1, -1):
        new_new_map[y + 1][c - 1] = new_map[y][c - 1]
    
    for x in range(0, c - 1):
        new_new_map[r - 1][x] = new_map[r - 1][x + 1]
    
    for y in range(air_r_2 + 1, r - 1):
        new_new_map[y][0] = new_map[y + 1][0]
    
    real_map = copy.deepcopy(new_new_map)
    real_map[air_r_1][air_c_1] = -1
    real_map[air_r_2][air_c_2] = -1

total = 0
for i in range(r):
    for j in range(c):
        if real_map[i][j] != -1:
            total += real_map[i][j]

print(total)