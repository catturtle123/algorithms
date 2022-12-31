n = int(input())

nlist = list(map(int,input().split()))

result = 0
for i in nlist:
    num = 0
    for j in range(1,i+1):
        if i % j == 0:
            num += 1
        if num > 3:
            break
    if num == 2:
        result += 1

print(result)
            