import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())

    temp = []
    temp2 = list(map(int, input().split()))
    for i in range(n):
        temp.append((temp2[i], i))
    
    queue = deque(temp)
    target = temp[m][1]
    cnt = 0
    while True:
        next = False
        value, node = queue.popleft()

        for i in queue:
            if value < i[0]:
                next = True
                queue.append((value, node))
                break
        
        if not next:
            cnt += 1
            if node == target:
                print(cnt)
                break