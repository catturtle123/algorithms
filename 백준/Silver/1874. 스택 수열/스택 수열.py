from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

queue = deque([])
for i in range(n):
    a = int(input())
    queue.append(a)

queue.append(0)

current = 1
stack = []
result = []
stop = False
a = queue.popleft()
while a != 0:
    if current <= a:
        stack.append(current)
        current += 1
        result.append("+")
    else:
        s = stack.pop()
        if s != a:
            stop = True
            break
        result.append("-")
        a = queue.popleft()

if stop:
    print("NO")
else:
    for i in result:
        print(i)