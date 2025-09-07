from collections import deque

def index_sort(x):
    return x[1]

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        q.append((food_times[i], i + 1))
    
    q.sort()
    
    prev = 0
    q = deque(q)
    total = 0
    
    while q:
        s = len(q)
        diff = q[0][0] - prev
        spend = diff * s
        
        if total + spend <= k:
            total += spend
            prev = q[0][0]
            q.popleft()
        else:
            break
    
    q = list(q)
    q = sorted(q, key=index_sort)
    return q[(k - total) % len(q)][1]