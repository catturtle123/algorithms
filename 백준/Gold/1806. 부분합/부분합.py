import sys
input = sys.stdin.readline
INF = sys.maxsize
 
s, r = map(int, input().split())
nlist = list(map(int, input().split()))

left = 0
right = 0
result = INF
current_sum = 0

while True:
    if current_sum >= r:
        result = min(result, right - left)
        current_sum -= nlist[left]
        left += 1
    elif right == s:
        break
    else:
        current_sum += nlist[right]
        right += 1

if result == INF:
    print(0)
else:
    print(result)