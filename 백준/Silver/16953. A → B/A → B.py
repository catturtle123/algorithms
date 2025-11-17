from collections import deque

def bfs(start, end):
    queue = deque([(start, 1)])

    while queue:
        q, result = queue.popleft()

        if q == end:
            return result

        if q * 2 <= end:
            queue.append((q * 2, result + 1))

        s = str(q) + str(1)
        if int(s) <= end:
            queue.append((int(s), result + 1))

    return -1

a, b = map(int, input().split())
print(bfs(a, b))