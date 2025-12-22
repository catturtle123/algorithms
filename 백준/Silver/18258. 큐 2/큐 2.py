import sys
from collections import deque
input = sys.stdin.readline

def push(x):
    queue.append(x)

def pop():
    if empty() == 1:
        return -1
    else:
        return queue.popleft()

def front():
    if empty() == 1:
        return -1
    else:
        return queue[0]
    
def back():
    if empty() == 1:
        return -1
    else:
        return queue[-1]

def empty():
    if size() == 0:
        return 1
    else:
        return 0
    
def size():
    return len(queue)

n = int(input())
queue = deque([])

for _ in range(n):
    s_list = list(map(str, input().split()))
    operation = s_list[0]

    if operation == "push":
        push(s_list[1])
    elif operation == "pop":
        print(pop())
    elif operation == "empty":
        print(empty())
    elif operation == "size":
        print(size())
    elif operation == "back":
        print(back())
    elif operation == "front":
        print(front())