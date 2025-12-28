a, b = map(int, input().split())

p = 10 + 2 * (25 - a + b)

if p <= 0:
    print(0)
else:
    print(p)