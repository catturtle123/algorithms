n = input()

s = 0
c = n

count = 0
while n != int(c):
    if int(n) < 10:
        n = "0" + str(n)[-1]    
    else:
        n = str(n)

    s = int(n[0]) + int(n[-1])
    if s >= 10:
        s = int(str(s)[-1])
    s += int(n[-1]) * 10
    n = int(s)
    count += 1


print(count)