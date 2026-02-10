n = int(input())

for i in range(n):
    s = " " * (n - i - 1) + "*" * (i) + "*" + "*" * (i)
    print(s)