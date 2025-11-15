def fun(num, expo):
    if expo == 1:
        return num % c
    
    temp = fun(num, expo // 2)

    if expo % 2 == 1:
        return (temp * temp * num) % c
    
    return (temp * temp) % c

a, b, c = map(int, input().split())

print(fun(a, b))