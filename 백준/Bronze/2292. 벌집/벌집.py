n = int(input())


if n == 1:
    print(1)


result = 2
for i in range(0,n+1):
    result += i*6


    if result <= n <= result+6*(i+1)-1:
        print(i+2)
        break

