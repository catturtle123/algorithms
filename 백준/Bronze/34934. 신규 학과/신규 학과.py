n = int(input())

for _ in range(n):
    a, b = map(str, input().split())
    if int(b) == 2026:
        print(a)
        