import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

answer = 0

def merge(line):
    line = [x for x in line if x != 0]
    result = []
    i = 0

    while i < len(line):
        if i + 1 < len(line) and line[i] == line[i + 1]:
            result.append(line[i] * 2)
            i += 2
        else:
            result.append(line[i])
            i += 1

    while len(result) < n:
        result.append(0)

    return result

def move(board, direction):
    new_board = [[0] * n for _ in range(n)]

    # 왼쪽
    if direction == 0:
        for y in range(n):
            new_board[y] = merge(board[y])

    # 오른쪽
    elif direction == 1:
        for y in range(n):
            new_board[y] = merge(board[y][::-1])[::-1]

    # 위
    elif direction == 2:
        for x in range(n):
            line = []
            for y in range(n):
                line.append(board[y][x])

            merged = merge(line)

            for y in range(n):
                new_board[y][x] = merged[y]

    # 아래
    elif direction == 3:
        for x in range(n):
            line = []
            for y in range(n):
                line.append(board[y][x])

            merged = merge(line[::-1])[::-1]

            for y in range(n):
                new_board[y][x] = merged[y]

    return new_board

def dfs(board, depth):
    global answer

    for y in range(n):
        for x in range(n):
            answer = max(answer, board[y][x])

    if depth == 5:
        return

    for direction in range(4):
        next_board = move(board, direction)
        dfs(next_board, depth + 1)

dfs(board, 0)
print(answer)