# 136, 142, 148, 154
n = int(input())

result = 0
for _ in range(n):
    a, b = map(int, input().split())
    
    if a == 136:
        result += 1000
    elif a == 142:
        result += 5000
    elif a == 148:
        result += 10000
    elif a == 154:
        result += 50000

print(result)