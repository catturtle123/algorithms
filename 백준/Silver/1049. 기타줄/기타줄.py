num,brand = map(int,input().split())

packageList = []
aList = []
for i in range(brand):
    a,b = map(int,input().split())
    packageList.append(a)
    aList.append(b)

packageList.sort()
aList.sort()

packagenum = num // 6
anum = num % 6

if num == 0:
    print(0)
else:
    if aList[0] * 6 < packageList[0]:
        print(aList[0]*num)
    else:
        if anum * aList[0] >= packageList[0]:
            print(packageList[0]*packagenum + packageList[0])
        else:
            print(packageList[0]*packagenum + anum * aList[0])