n = input()
s = ""

for i in n:
    if i.isalpha():
        s += i

n = input()

if n in s:
    print(1)
else:
    print(0)