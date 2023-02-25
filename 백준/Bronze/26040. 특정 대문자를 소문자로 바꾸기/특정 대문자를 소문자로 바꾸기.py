s = input()
slist = list(map(str,input().split()))

str1 = ""
for i in s:
    if i in slist:
        str1 += chr(ord(i)+32)
    else:
        str1 += i

print(str1)