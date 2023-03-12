n = int(input())

count = 0
for i in range(n):
    s = input()
    if s == "anj":
        print("뭐야;")
        count  = 1
        break

if count != 1:
    print("뭐야?")
