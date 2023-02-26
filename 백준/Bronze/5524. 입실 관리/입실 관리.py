n = int(input())

for i in range(n):
    s = input()
    for i in s:
        if i.isupper():
            print(i.lower(),end="")
        else:
            print(i,end="")
    print()