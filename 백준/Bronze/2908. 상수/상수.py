a,b = map(int,input().split())

nlist1 = []
for i in str(a):
    nlist1.append(int(i))

nlist2 = []
for i in str(b):
    nlist2.append(int(i))

nlist1[0], nlist1[2] = nlist1[2], nlist1[0]
nlist2[0], nlist2[2] = nlist2[2], nlist2[0]


o = 100
result1 = 0
for i in nlist1:

    result1 += i*o
    o /= 10

a = int(result1)

o = 100
result2 = 0
for i in nlist2:
    result2 += i*o
    o /= 10


b = int(result2)


if a > b:
    print(a)
else:
    print(b)