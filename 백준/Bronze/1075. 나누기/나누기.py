a = input()
b = int(input())
d = ""
a = list(a)

a[-2] = "0"
a[-1] = "0"

for i in a:
    d += i

a = int(d)

while True:
    if a % b == 0:
        break
    a += 1

a = list(str(a))
print(f"{a[-2]}{a[-1]}")