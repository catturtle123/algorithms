n = input()

s = ""
for i in n:
    if i.isalpha():
        s += i

y = input()
if y in s:
    print(1)
else:
    print(0)