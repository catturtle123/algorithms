s = input()

if len(s) == 2:
    print(int(s[0]) + int(s[1]))
elif len(s) == 3:
    if s[1] == "0":
        print(int(s[0:2]) + int(s[1:3]))
    else:
        print(int(s[0]) + int(s[1:3]))
elif len(s) == 4:
    print(int(s[0:2]) + int(s[2:4]))