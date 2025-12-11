# 빙고판에 1~25까지 존재
# 사회자가 숫자 하나씩 부르면서 지워나감
# 3줄 이상 생기고 가장 먼저 "빙고"를 외치면 이김
# 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는 지 출력

import sys
input = sys.stdin.readline

def is_bingo():
    bingo_num = 0

    for y in range(5):
        is_bin = True
        for x in range(5):
            if bingo[y][x] != 1:
                is_bin = False
        
        if is_bin:
            bingo_num += 1

    for y in range(5):
        is_bin = True
        for x in range(5):
            if bingo[x][y] != 1:
                is_bin = False
        
        if is_bin:
            bingo_num += 1

    for i in range(5):
        is_bin = True
        if bingo[i][i] != 1:
            is_bin = False
            break
        
    if is_bin:
        bingo_num += 1

    for i in range(5):
        is_bin = True
        if bingo[4 - i][i] != 1:
            is_bin = False
            break
        
    if is_bin:
        bingo_num += 1

    return bingo_num

maps = []
for i in range(5):
    temp = list(map(int, input().split()))
    maps.append(temp)

bingo = [[0] * 5 for _ in range(5)]

cnt = 1
is_break = False
while True:
    ns = list(map(int, input().split()))

    for n in ns:
        for i in range(5):
            for j in range(5):
                if maps[i][j] == n:
                    bingo[i][j] = 1
        
        if is_bingo() >= 3:
            print(cnt)
            is_break = True
            break

        cnt += 1
    
    if is_break:
        break