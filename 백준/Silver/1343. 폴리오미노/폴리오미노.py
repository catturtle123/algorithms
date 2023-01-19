n = input()


count = 0
result = ""
xlist = []
if n.count("X") % 2 != 0:
    print(-1)
else:
    for i in n:
        if i == ".":
            xlist.append(result)
            xlist.append(".")
            result = ""
        if i != ".":
            result += i
    xlist.append(result)

result = ""
for i in xlist:
    four = len(i) // 4
    a = len(i) % 4
    two = a // 2
    if i != '.':
        if len(i) % 2 != 0:
            result = "-1"
            break
        result += four * "AAAA" + two * "BB"
    if i == '.':
        result += '.'
    if i == "":
        pass

print(result)