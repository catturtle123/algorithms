import sys
input = sys.stdin.readline

n = int(input())
price = list(map(int, input().split()))
m = int(input())

# 0이 아닌 숫자 중 가장 싼 숫자 찾기
first = -1
for i in range(1, n):
    if first == -1 or price[i] < price[first] or (price[i] == price[first] and i > first):
        first = i

# 0~n-1 중 가장 싼 숫자 찾기
cheap = 0
for i in range(n):
    if price[i] < price[cheap] or (price[i] == price[cheap] and i > cheap):
        cheap = i

# 첫 자리를 만들 수 없으면 0만 가능
if price[first] > m:
    print(0)
    exit()

# 일단 최대 길이 만들기
result = [first]
m -= price[first]

while m >= price[cheap]:
    result.append(cheap)
    m -= price[cheap]

# 왼쪽부터 최대한 큰 숫자로 교체
for i in range(len(result)):
    now = result[i]
    for d in range(n - 1, -1, -1):
        need = price[d] - price[now]
        if need <= m:
            result[i] = d
            m -= need
            break

print(''.join(map(str, result)))