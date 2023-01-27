n = input()
mlist = ["a","e","i","o","u"]

count = 0
for i in n:
    for j in mlist:
        if i == j:
            count += 1


print(count)