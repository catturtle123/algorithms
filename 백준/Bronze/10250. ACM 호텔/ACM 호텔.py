n = int(input())


w = 0
h = 0
for i in range(n):
    a,b,c = map(int,input().split())
    h = c%a
    if c % a == 0:
        h = a
    w = c//a + 1
    if c % a == 0:
       w = c//a
    if w < 10:
        w = "0" + str(w)
    
    print(str(h)+str(w))