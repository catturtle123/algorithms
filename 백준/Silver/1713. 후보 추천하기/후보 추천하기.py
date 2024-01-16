dic = {}
n = int(input())
s = input()
nlist = list(map(int, input().split(' ')))
minlist = []
min = 100
count = 0

for i in nlist:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

    if len(dic) > n:
        for j in dic:
            count += 1
            if count > n:
                break
            if min > dic[j]:
                min = dic[j]
                minlist = []
                minlist.append(j)
            else:
                minlist.append(j)
    
        del dic[minlist[0]]
        minlist = []
        min = 100
    count = 0

sorted_dict = sorted(dic)

for i in sorted_dict:
    print(i, end=' ')