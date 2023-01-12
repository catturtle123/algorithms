a,b,c = map(int,input().split())

if a == b == c:
    print(10000+a*1000)
elif a != b and b != c and a != c:
    d = max(a,b,c)
    print(100*d)
else:
    if a == b:
        d = a
    elif b == c:
        d = b
    elif a == c:
        d = a
    print(1000+d*100)