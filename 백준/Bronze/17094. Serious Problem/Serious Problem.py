n = int(input())
n = input()

number = n.count("2")
e = n.count("e")

if number > e:
    print(2)
elif number < e:
    print("e")
else:
    print("yee")