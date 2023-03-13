n = int(input())

for i in range(n):
    s = input()
    o = ""

    for j in s:
        if ord(j) != ord("Z"):
            o += chr(ord(j)+1)
        else:
            o += "A"

    print(f"String #{i+1}\n{o}\n")