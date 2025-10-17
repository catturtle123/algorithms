import sys
input = sys.stdin.readline

m, n = map(int, input().split())
array = [True] * (n + 1)
array[0] = False
array[1] = False

for i in range(2, n + 1):
    if array[i]:

        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(m, n + 1):
    if array[i]:
        print(i)