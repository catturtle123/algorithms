import sys, bisect
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
temp_list = []
temp_list.append(nlist[0])

for i in range(1, len(nlist)):
    if temp_list[-1] < nlist[i]:
        temp_list.append(nlist[i])
    else:
        temp_right_index = bisect.bisect_left(temp_list, nlist[i])
        temp_list[temp_right_index] = nlist[i]

print(len(temp_list))  