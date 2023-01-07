n = int(input())

sum = 1
for i in range(1,n+1):
    sum *= i

sum = str(sum)
sumList = []
for i in sum:
    sumList.append(int(i))

sumList.reverse()

sum2 = 0
for i in sumList:
    if i == 0:
        sum2 += 1
    else:
        break

print(sum2)