n = int(input())

result = n // 5
temp = n % 5

if temp == 0:
    print(result)
else:
    print(result + 1)