import sys
input = sys.stdin.readline

n = int(input())
nlist = []

for i in range(n):
    nlist.append(list(map(int, input().split())))

for i in range(n - 1):
    temp_list1 = []
    temp_list2 = []
    temp_list3 = []
    for j in range(3):
        if j == 0:
            temp2 = nlist[i][j] + nlist[i + 1][j + 1]
            temp3 = nlist[i][j] + nlist[i + 1][j + 2]

            temp_list2.append(temp2)
            temp_list3.append(temp3)
        elif j == 1:
            temp1 = nlist[i][j] + nlist[i + 1][j - 1]
            temp3 = nlist[i][j] + nlist[i + 1][j + 1]

            temp_list1.append(temp1)
            temp_list3.append(temp3)
        elif j == 2:
            temp2 = nlist[i][j] + nlist[i + 1][j - 1]
            temp1 = nlist[i][j] + nlist[i + 1][j - 2]

            temp_list1.append(temp1)
            temp_list2.append(temp2)
    
    nlist[i + 1][0] = min(temp_list1)
    nlist[i + 1][1] = min(temp_list2)
    nlist[i + 1][2] = min(temp_list3)
            

print(min(nlist[n - 1]))