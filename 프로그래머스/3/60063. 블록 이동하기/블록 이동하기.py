from collections import deque

def solution(board):
    n = len(board[0])

    visited = []

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    queue = deque([])
    queue.append(((0, 0), (0, 1), 0))
    visited.append(((0,0), (0,1)))

    while queue:
        (y1, x1), (y2, x2), value = queue.popleft()

        if (y1, x1) == (n-1, n-1) or (y2, x2) == (n-1, n-1):
            return value

        # 상, 하, 좌, 우로 움직일 때
        for i in range(4):
            ny1, nx1, ny2, nx2 = y1 + dy[i], x1 + dx[i], y2 + dy[i], x2 + dx[i] 

            # 맵 끝일 때
            if 0 <= ny1 < n and 0 <= nx1 < n and 0 <= ny2 < n and 0 <= nx2 < n:
                # 벽이 아닐 때
                if board[ny1][nx1] != 1 and board[ny2][nx2] != 1:

                    if ((ny1, nx1), (ny2, nx2)) not in visited:
                        visited.append(((ny1, nx1), (ny2, nx2)))
                        visited.append(((ny2, nx2), (ny1, nx1)))

                        queue.append(((ny1, nx1), (ny2, nx2), value + 1))
        
        # 회전할 때
        # 가로 상태
        if y1 == y2:
            for ay in [-1, 1]:
                if 0<= y1 + ay < n and 0 <= x1 < n and 0 <= y2 + ay < n and 0 <= x2 < n:
                    if board[y1 + ay][x1] == 0 and board[y2 + ay][x2] == 0:
                        for i in [((y1 + ay, x2), (y2, x2)), ((y1, x1), (y2 + ay, x1))]:
                            ny1 = i[0][0]
                            nx1 = i[0][1]
                            ny2 = i[1][0]
                            nx2 = i[1][1]

                            if not (0 <= ny1 < n and 0 <= nx1 < n and 0 <= ny2 < n and 0 <= nx2 < n):
                                continue

                            if ((ny1, nx1), (ny2, nx2)) not in visited:
                                visited.append(((ny1, nx1), (ny2, nx2)))
                                visited.append(((ny2, nx2), (ny1, nx1)))

                                queue.append(((ny1, nx1), (ny2, nx2), value + 1))

        # 세로 상태
        if x1 == x2:
            for ax in [-1, 1]:
                if 0<= y1 < n and 0 <= x1 + ax < n and 0 <= y2 < n and 0 <= x2 + ax < n:
                    if board[y1][x1 + ax] == 0 and board[y2][x2 + ax] == 0:
                        for i in [((y2, x1 + ax), (y2, x2)), ((y1, x1), (y1 , x2 + ax))]:
                            ny1 = i[0][0]
                            nx1 = i[0][1]
                            ny2 = i[1][0]
                            nx2 = i[1][1]

                            if not (0 <= ny1 < n and 0 <= nx1 < n and 0 <= ny2 < n and 0 <= nx2 < n):
                                continue

                            if ((ny1, nx1), (ny2, nx2)) not in visited:
                                visited.append(((ny1, nx1), (ny2, nx2)))
                                visited.append(((ny2, nx2), (ny1, nx1)))

                                queue.append(((ny1, nx1), (ny2, nx2), value + 1))