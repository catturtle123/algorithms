n = int(input())
nlist = []
for _ in range(n):
    a = input()
    nlist.append((ord(a[0]) - ord('A'), int(a[1:]) - 1))



for i in range(10):
    for j in range(20):
        if (i, j) in nlist:
            print("o", end="")
        else:
            print(".", end="")

    print()