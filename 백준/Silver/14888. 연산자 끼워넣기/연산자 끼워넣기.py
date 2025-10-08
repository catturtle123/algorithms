# 2초, 512MB

# 주어진 수를 바꾸면 안됨
# 중간에 연산자를 넣을 수 있음
# 연산자의 우선 순위를 무시하고 앞에서 부터 계산
# 음수에서 양수를 나눌때는 양수로 바꾼뒤 몫을 취하고 그 몫을 음수로 바꾼 것과 같다
# 최소 값과 최대 값을 구하라
# 최소 값은 가장 큰 값끼리 곱하고 가장 작은 값끼리 뺀것
# 완전 탐색, dfs

def dfs(i, olist, sum):
    global max_sum
    global min_sum

    # 종료 조건
    if i == n:
        max_sum = max(max_sum, sum)
        min_sum = min(min_sum, sum)
        return

    # +
    if olist[0] > 0:
        olist[0] -= 1
        dfs(i + 1, olist, sum + nlist[i])
        olist[0] += 1

    # -
    if olist[1] > 0:
        olist[1] -= 1
        dfs(i + 1, olist, sum - nlist[i])
        olist[1] += 1

    # *
    if olist[2] > 0:
        olist[2] -= 1
        dfs(i + 1, olist, sum * nlist[i])
        olist[2] += 1

    # /
    if olist[3] > 0:
        olist[3] -= 1
        
        new_sum = 0
        if sum < 0:
            new_sum = -(-sum // nlist[i])
        else:
            new_sum = sum // nlist[i]
        
        dfs(i + 1, olist, new_sum)
        olist[3] += 1

import sys
input = sys.stdin.readline

# 입력
n = int(input())

nlist = list(map(int, input().split(" "))) # 각 숫자
olist = list(map(int, input().split(" "))) # 각 연산자의 갯수 +, -, *, /

max_sum = -1_000000000000
min_sum = 1_000_000_000_000
dfs(1, olist, nlist[0])

print(max_sum)
print(min_sum)