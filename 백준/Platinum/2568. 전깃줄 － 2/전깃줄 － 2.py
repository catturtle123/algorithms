import sys, bisect
input = sys.stdin.readline

def binary_search(b_list, x):
    start = 0
    end = len(b_list) - 1

    while start < end:
        mid = (start + end) // 2

        if b_list[mid][1] < x:
            start = mid + 1 
        else:
            end = mid
    
    return start

n = int(input())
nlist = []
for _ in range(n):
    a, b = map(int, input().split())
    nlist.append((a, b))

nlist.sort(key=lambda x:x[0])
temp_list = []
temp_list.append(nlist[0])
pos = [0] * (len(nlist) + 1)

for i in range(1, len(nlist)):
    if temp_list[-1][1] < nlist[i][1]:
        temp_list.append(nlist[i])
        pos[i] = len(temp_list) - 1
    else:
        temp_right_index = binary_search(temp_list, nlist[i][1])
        temp_list[temp_right_index] = nlist[i]
        pos[i] = temp_right_index

target = len(temp_list) - 1
trash = set()

for i in range(n - 1, -1, -1):
    if pos[i] == target:
        trash.add(nlist[i][0])
        target -= 1

print(n - len(temp_list))  
for i in nlist:
    if i[0] not in trash:
        print(i[0])