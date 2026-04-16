import sys, bisect
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
temp_list = []
temp_list.append(nlist[0])
pos = [0] * (len(nlist) + 1)

for i in range(1, len(nlist)):
    if temp_list[-1] < nlist[i]:
        temp_list.append(nlist[i])
        pos[i] = len(temp_list) - 1
    else:
        temp_right_index = bisect.bisect_left(temp_list, nlist[i])
        temp_list[temp_right_index] = nlist[i]
        pos[i] = temp_right_index

target = len(temp_list) - 1
answer = []

for i in range(n - 1, -1, -1):
    if pos[i] == target:
        answer.append(nlist[i])
        target -= 1

answer.reverse()

print(len(temp_list))  
for i in answer:
    print(i, end=" ")