# 수열이 주어졌을때 가장 긴 감소하는 부분의 수열을 구하시오

import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))

# 자기 보다 작은 값에 1씩 더해주기
result_list = [1] * (n)

# 부분의 작은 값이 대표값이 된다
# 10 30 10 20 20 10
# 1  1  2  2  2  3

for i in range(n):
    for j in range(i + 1, n):
        if nlist[i] > nlist[j]:
            result_list[j] = max(result_list[i] + 1, result_list[j])

print(max(result_list))