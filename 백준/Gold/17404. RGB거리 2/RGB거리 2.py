# 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

import sys, copy
input = sys.stdin.readline

n = int(input())
nlist = []
for _ in range(n):
    temp = list(map(int, input().split()))
    nlist.append(temp)


# 1회차
temp_list = copy.deepcopy(nlist)
first = temp_list[0][0]
temp_list[1][1] += first
temp_list[1][2] += first
temp_list[1][0] = sys.maxsize
for i in range(2, n):
    temp_list[i][0] = min(temp_list[i - 1][1], temp_list[i - 1][2]) + temp_list[i][0]
    temp_list[i][1] = min(temp_list[i - 1][2], temp_list[i - 1][0]) + temp_list[i][1]
    temp_list[i][2] = min(temp_list[i - 1][0], temp_list[i - 1][1]) + temp_list[i][2]

temp_result = min(temp_list[n - 1][1], temp_list[n - 1][2])

# 2회차
temp_list = copy.deepcopy(nlist)
first = temp_list[0][1]
temp_list[1][0] += first
temp_list[1][2] += first
temp_list[1][1] = sys.maxsize
for i in range(2, n):
    temp_list[i][0] = min(temp_list[i - 1][1], temp_list[i - 1][2]) + temp_list[i][0]
    temp_list[i][1] = min(temp_list[i - 1][2], temp_list[i - 1][0]) + temp_list[i][1]
    temp_list[i][2] = min(temp_list[i - 1][0], temp_list[i - 1][1]) + temp_list[i][2]

temp_result = min(temp_list[n - 1][0], temp_list[n - 1][2], temp_result)

# 3회차
temp_list = copy.deepcopy(nlist)
first = temp_list[0][2]
temp_list[1][1] += first
temp_list[1][0] += first
temp_list[1][2] = sys.maxsize
for i in range(2, n):
    temp_list[i][0] = min(temp_list[i - 1][1], temp_list[i - 1][2]) + temp_list[i][0]
    temp_list[i][1] = min(temp_list[i - 1][2], temp_list[i - 1][0]) + temp_list[i][1]
    temp_list[i][2] = min(temp_list[i - 1][0], temp_list[i - 1][1]) + temp_list[i][2]

temp_result = min(temp_list[n - 1][0], temp_list[n - 1][1], temp_result)

print(temp_result)