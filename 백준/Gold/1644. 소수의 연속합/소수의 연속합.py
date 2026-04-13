# 연속된 소수의 합으로 나타낼 수 있는 경우의 수
import sys, math
input = sys.stdin.readline

# 소수인지 확인
n = int(input())

if n == 1:
    print(0)
    exit(0)

is_prime_list = [True] * (n + 1)
is_prime_list[0] = False
is_prime_list[1] = False

for i in range(2, int(math.sqrt(n) + 1)):
    if is_prime_list[i] == True:
        j = 2

        while (i * j) <= n:
            is_prime_list[i * j] = False
            j += 1

temp_list = [0]
for i in range(2, n + 1):
    if is_prime_list[i] == True:
        temp_list.append(i)

# 누적합
for i in range(1, len(temp_list)):
    temp_list[i] = temp_list[i] + temp_list[i - 1]

# 투포인터
result = 0
i = 0
j = 1
while True:
    temp = temp_list[j] - temp_list[i]

    if temp == n:
        result += 1
        j += 1
    elif temp < n:
        j += 1
    else:
        i += 1

    if i >= j or j >= len(temp_list):
        break

print(result)