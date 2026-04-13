# 온도의 합이 가장 큰 값을 알아보자
import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 전체 날짜의 수, 연속적인 날짜
nlist = list(map(int, input().split()))

# 누적합
nlist.insert(0, 0)
for i in range(1, len(nlist)):
    nlist[i] = nlist[i] + nlist[i - 1]

# 각 자리 수 마다의 값을 저장
i = 0
j = k
result = -(100_000 * 100 + 1) 
while j <= n:
    result = max(result, nlist[j] - nlist[i])
    i += 1
    j += 1

# 가장 큰값 출력
print(result)