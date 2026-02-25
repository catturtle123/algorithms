n, m = map(int, input().split())

if n > m:
    print(m + 1 + m)
else:
    print(n + n - 1)