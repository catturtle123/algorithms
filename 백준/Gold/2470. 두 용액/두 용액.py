import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))

nlist.sort()
i = 0
j = n - 1
result = sys.maxsize
result_list = []

while True:
    temp = nlist[i] + nlist[j]

    temp_value = abs(temp)
    if result > temp_value:
        result = temp_value
        result_list = [nlist[i], nlist[j]]


    if temp == 0:
        break
    elif temp < 0:
        i += 1
    else:
        j -= 1



    if i >= j:
        break

result_list.sort()
for i in result_list:
    print(i, end=" ")