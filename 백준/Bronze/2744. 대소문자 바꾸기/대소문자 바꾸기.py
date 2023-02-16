n = input()

for i in n:
    if i.islower():
        print(chr(ord(i)-32),end="")
    else:
        print(chr(ord(i)+32),end="")