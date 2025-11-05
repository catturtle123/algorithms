import sys
input = sys.stdin.readline


def board_search(start):
    y = start[0]
    x = start[1]
    start_str = start[2]

    result = 0
    # 시작 부터 8칸 탐색
    for i in range(y, y + 8):
        for j in range(x, x + 8):
            current = board[i][j]

            # 짝수일 때 다르면 +1
            if (i + j - y - x) % 2 == 0 and start_str != current:
                result += 1
            elif (i + j - y - x) % 2 != 0 and start_str == current:
                result += 1

              
    return result

n, m = map(int, input().split())
board = []

for i in range(n):
    s = input().rstrip()
    temp = []
    for j in s:
        temp.append(j)

    board.append(temp)

min_result = sys.maxsize
for i in range(n):
    for j in range(m):
        if i + 8 > n or j + 8 > m:
            continue

        result = board_search((i, j, "W"))
        if min_result >  result:
            min_result = result

        result = board_search((i, j, "B"))
        if min_result >  result:
            min_result = result

print(min_result)
           