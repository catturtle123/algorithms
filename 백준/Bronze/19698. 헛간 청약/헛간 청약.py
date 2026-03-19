n, w, h, l = map(int, input().split())

y = w // l
x = h // l
location = y * x

if n < location:
    print(n)
else:
    print(location)