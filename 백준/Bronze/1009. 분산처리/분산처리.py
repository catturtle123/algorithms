n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    a = int(str(a)[-1])
    if a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 3 or a == 2 or a == 7 or a == 8:
       if b % 4 == 1:
        print(a)
       elif b % 4 == 0:
        print(str(a**4)[-1])
       else:
        print(str(a ** (b % 4))[-1])  
    elif a == 4 or a == 9:
       if b % 2 == 1:
        print(a)
       elif b % 2 == 0:
        print(str(a**2)[-1])
       else:
        print(str(a ** (b % 2))[-1])
    elif a == 0:
        print(10)

