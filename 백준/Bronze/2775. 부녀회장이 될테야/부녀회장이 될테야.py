import sys
input = sys.stdin.readline

apart = [[0] * 14 for _ in range(15)]
for i in range(14):
    apart[0][i] = (i + 1)

for i in range(1, 15):
    for j in range(14):
        apart[i][j] = sum(apart[i - 1][:j + 1])

t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())

    print(apart[k][n - 1])