import sys
input = sys.stdin.readline

# 입력
n = int(input())
nlist = list(map(int, input().split()))

# 초기 포인터 값
first = 0
last = len(nlist) - 1

# 최댓 값
result = sys.maxsize

# 결과 값
current = 0
result1 = 0
result2 = 0

while first < last:
    
    # 현재 값
    current = nlist[first] + nlist[last]

    # current의 절댓값이 더 작다면 result에 대입
    if result > abs(current):
        result = abs(current)
        result1 = nlist[first]
        result2 = nlist[last]

    if current == 0:
        break

    # current 값이 음수라면 first를 +, 양수라면 last를 -1
    if current < 0:
        first += 1
    else:
        last -= 1

print(result1, result2)