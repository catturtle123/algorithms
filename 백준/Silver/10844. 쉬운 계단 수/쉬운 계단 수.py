n = int(input())
nlist = [[0] * 10 for _ in range(n + 1)]

mod = 1_000_000_000

for i in range(1, 10):
    nlist[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            nlist[i][j] = nlist[i - 1][1]
        elif j == 9:
            nlist[i][j] = nlist[i - 1][8]
        else:
            nlist[i][j] = nlist[i - 1][j - 1] + nlist[i - 1][j + 1]

sum = 0
for i in nlist[n]:
    sum += i

print(sum % mod)