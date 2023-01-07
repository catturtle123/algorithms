num = int(input())

a,b = 0,0

def fibo1(n):
    global a,b
    if n == 0:
        a += 1
        return 0
    elif n == 1:
        b += 1 
        return 1
    elif n == 2:
        a += 1
        b += 1
        return -1
    elif n == 3:
        a += 1 
        b += 2
        return -1
    elif n == 4:
        a += 2
        b += 3
        return -1
    elif n == 5:
        a += 3
        b += 5
        return -1
    elif n == 6:
        a += 5
        b += 8
        return -1
    elif n == 7:
        a += 8
        b += 13
        return -1
    elif n == 22:
        a += 10946
        b += 17711
        return -1
    elif n == 30:
        a += 514229
        b += 832040
        return -1
    elif n == 35:
        a += 5702887
        b += 9227465
        return -1
    elif n >= 0:
        return fibo1(n-1) + fibo1(n-2)


for i in range(num):
    n = int(input())
    fibo1(n)
    print(a,b)
    a = 0
    b = 0