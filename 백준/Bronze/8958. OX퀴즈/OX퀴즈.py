n = int(input())


for i in range(n):
    ox = input()
    sum = 0
    l = 0
    for i in ox:
        if "O" == i:
            sum += 1+l
            l += 1
        else:
            l = 0
    print(sum)