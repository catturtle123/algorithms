import sys
import queue
input = sys.stdin.readline

n = int(input())
maps = [[0] * (n + 1) for _ in range(n + 1)]

apple_num = int(input())
apple_list = []
for i in range(apple_num):
    y, x = map(int, input().split(" "))
    maps[y][x] = 1
    apple_list.append((y, x))

direct = []
direct_num = int(input())
for i in range(direct_num):
    second, text = input().split(" ")
    direct.append((int(second), text))

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)] # N, E, S, W
dir_num = 1
maps[1][1] = 2
current_y = 1
current_x = 1
current_temp_y = 1
current_temp_x = 1
current_second = 0
current_list = []
length = 1
temp_length = 0

while True:
    temp_length = 1

    # 나아갈 위치 지정
    for i in direct:
        second, d_dir = i[0], i[1].rstrip()
        if current_second == second:
            if d_dir == 'D':
                dir_num += 1
                if dir_num == 4:
                    dir_num = 0
            else:
                dir_num -= 1
                if dir_num == -1:
                    dir_num = 3

    # 다음 지점
    current_temp_y += dir[dir_num][0]
    current_temp_x += dir[dir_num][1]

    # 현재 지점 맞는 지 확인
    if current_temp_y <= 0 or current_temp_y > n or current_temp_x <= 0 or current_temp_x > n:
        break

    # 다음 지점이 자기 자신인지
    if maps[current_temp_y][current_temp_x] == 2:
        break

    # 마지막 지점 사과인지에 따라 처리
    if maps[current_temp_y][current_temp_x] == 1:
        apple_list.remove((current_temp_y, current_temp_x))
        length += 1
    
    # 다음 지점을 자기 지점으로 돌리기
    current_y = current_temp_y
    current_x = current_temp_x
    current_list.append([current_y, current_x])

    # 실질적 움직이기
    maps = [[0] * (n + 1) for _ in range(n + 1)]
    for i in apple_list:
        maps[i[0]][i[1]] = 1
    for i in range(len(current_list) - 1, -1, -1):
        if temp_length <= length:
            maps[current_list[i][0]][current_list[i][1]] = 2
            temp_length += 1
        else:
            break

    current_second += 1

print(current_second + 1)