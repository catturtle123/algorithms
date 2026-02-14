t = int(input())

for _ in range(t):
    n, a, d = map(int, input().split())

    result = 0

    for i in range(n):
        temp = a + (d * i)
        result += temp


    print(result)