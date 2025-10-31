import sys
input = sys.stdin.readline

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

# N, M, k
n, m, k = map(int, input().split())

maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

# 초기 방향 (위, 아래, 왼쪽, 오른쪽)
intial_dir = list(map(int, input().split()))

# 각 상어의 방향 우선 순위 (상어번호 × 현재방향 × 4)
first_dir = [[] for _ in range(m + 1)]
for i in range(1, m + 1):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    first_dir[i] = temp

# 상어 정보 (번호, y, x, dir)
temp_shark = []
for i in range(n):
    for j in range(n):
        if maps[i][j] != 0:
            temp_shark.append([maps[i][j], i, j, intial_dir[maps[i][j] - 1]])

# 냄새 정보 [상어번호, 남은시간]
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]

time = 0
while True:
    # 기존 위치에 냄새를 뿌림
    for s in temp_shark:
        num, y, x, _ = s
        smell[y][x] = [num, k]

    new_shark = []
    # 4방향(우선 순위에 따라) 중 빈칸이 있는 지 확인
    for i in range(len(temp_shark)):
        num, y, x, d = temp_shark[i]
        moved = False
        for nd in first_dir[num][d - 1]:
            ny, nx = y + dy[nd], x + dx[nd]
            if 0 <= ny < n and 0 <= nx < n and smell[ny][nx][1] == 0:
                new_shark.append([num, ny, nx, nd])
                moved = True
                break
        # 없다면 자신의 냄새가 있는 곳으로 이동
        if not moved:
            for nd in first_dir[num][d - 1]:
                ny, nx = y + dy[nd], x + dx[nd]
                if 0 <= ny < n and 0 <= nx < n and smell[ny][nx][0] == num:
                    new_shark.append([num, ny, nx, nd])
                    break

    # 임시 저장한 위치를 확인해서 상어끼리 겹치는 것이 있으면 없앰 (작은 번호가 살아남음)
    new_shark.sort()
    temp = {}
    temp_shark = []
    for s in new_shark:
        num, y, x, d = s
        if (y, x) not in temp:
            temp[(y, x)] = num
            temp_shark.append([num, y, x, d])

    # 시간이 지난 냄새를 없앰
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j][0] = 0

    time += 1
    if len(temp_shark) == 1 and temp_shark[0][0] == 1:
        print(time)
        break
    if time >= 1000:
        print(-1)
        break
