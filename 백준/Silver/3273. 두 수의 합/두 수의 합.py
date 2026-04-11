# n개의 수열이 있다
# 각각의 1 <= x <= 1_000_000
# ai + aj = x을 만족하는 프로그램을 구하시오
# i < j

import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
x = int(input())

nlist.sort()

i = 0
j = n - 1
result = 0
while True:
    temp = nlist[i] + nlist[j]

    if temp == x:
        result += 1
        j -= 1
    elif temp > x:
        j -= 1
    else:
        i += 1
    
    if i >= j or j < 0 or j >= n:
        break

print(result)