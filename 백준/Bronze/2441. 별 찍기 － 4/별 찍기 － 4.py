n = int(input())

for i in range(1, n + 1):
    s = " " * (i - 1) + "*" * (n + 1 - i)
    print(s)