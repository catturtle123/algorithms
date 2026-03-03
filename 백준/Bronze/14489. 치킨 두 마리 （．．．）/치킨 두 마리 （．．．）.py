a, b = map(int, input().split())
pl = int(input())

if a + b < pl * 2:
    print(a + b)
else:
    print(a + b - pl * 2)