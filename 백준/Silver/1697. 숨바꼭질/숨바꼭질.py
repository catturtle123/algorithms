from collections import deque

n, k = map(int, input().split())

visited = [False] * 200_001

def bfs(start):
    queue = deque(start)

    # 현재 위치, 얼마나 갔는지
    while queue:
        current_pos, time = queue.popleft()

        # 만약 해당 위치로 갔다면 print & break
        if current_pos == k:
            print(time)
            break
        
        if 0 <= current_pos <= 100_000:
            if not visited[current_pos - 1]:
                visited[current_pos - 1] = True
                queue.append((current_pos - 1, time + 1))
            
            if not visited[current_pos + 1]:
                visited[current_pos + 1] = True
                queue.append((current_pos + 1, time + 1))
            
            if not visited[current_pos * 2]:
                visited[current_pos * 2] = True
                queue.append((current_pos * 2, time + 1))

bfs([(n, 0)])