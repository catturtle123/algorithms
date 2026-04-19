a, b = map(int, input().split())
nlist = list(map(int, input().split()))

for i in nlist:
    print(i - (a * b), end=" ")