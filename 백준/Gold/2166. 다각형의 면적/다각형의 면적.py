# 2차원 평면상 N개의 점으로 이루어진 다각형 -> 면적 구하기
# 입력 조건 -> N, N개의 점, 3 <= N <= 10000
# 면적 출력 -> 소수점 아래 둘째 자리에서
# nlogn 이하, 삼각형, 사각형, 오각형, 만각형

import sys
input = sys.stdin.readline

# 다각형의 면적을 구하기
n = int(input())

figure = []
for _ in range(n):
    y, x = map(int, input().split())
    figure.append((y, x))

sums = 0
for i in range(n):
    if i == n - 1:
        sums += (figure[0][1] * figure[n - 1][0] - figure[n - 1][1] * figure[0][0])
    else:
        sums += (figure[i][0] * figure[i + 1][1] - figure[i + 1][0] * figure[i][1])

print(abs(sums)/2)