import sys, copy
input = sys.stdin.readline

n, m = map(int, input().split())

def count_board(y, x):
    mins = sys.maxsize
    pattern = ["W", "B"]

    for start_color in pattern:
        fail = 0
        if start_color == "W":
            for i in range(8):
                for j in range(8):
                    if (i + j) % 2 == 0:
                        if board[y + i][x + j] != "W":
                            fail += 1
                    if (i + j) % 2 == 1:
                        if board[y + i][x + j] != "B":
                            fail += 1
        else:
            for i in range(8):
                for j in range(8):
                    if (i + j) % 2 == 0:
                        if board[y + i][x + j] != "B":
                            fail += 1
                    if (i + j) % 2 == 1:
                        if board[y + i][x + j] != "W":
                            fail += 1

        mins = min(mins, fail)

    return mins

board = []
for i in range(n):
    s = input().rstrip()
    temp = []
    for j in s:
        temp.append(j)
    board.append(temp)

mins = sys.maxsize
for i in range(n):
    for j in range(m):
        if 0 <= i <= n and 0 <= j <= m and 0 <= i + 8 <= n and 0 <= j + 8 <= m:
            fail = count_board(i, j)
            if mins > fail:
                mins = fail

print(mins)