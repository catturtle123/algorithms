n = int(input())
nlist = list(map(int,input().split()))

count = 0
count2 = 0

for i in nlist:
    if count == 3:
        count = 0

    if i == count:
        count2 += 1
        count += 1

print(count2)