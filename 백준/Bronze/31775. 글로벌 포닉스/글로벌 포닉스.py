nlist = []
for _ in range(3):
    s = input()
    nlist.append(s[0])

if "l" in nlist and "p" in nlist and "k" in nlist:
    print("GLOBAL")
else:
    print("PONIX")