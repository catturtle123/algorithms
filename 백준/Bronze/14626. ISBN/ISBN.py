n = input()

total = 0

a = 1
for index in range(len(n)):
    if n[index] == "*":
        if index % 2 == 0:
            a = 1
        else:
            a = 3
        continue

    temp = 0
    if index % 2 == 0:
        temp = int(n[index])
    else:
        temp = int(n[index]) * 3

    total += temp

for i in range(10):
    b = ((total + (i * a)) % 10)

    if b == 0:
        print(i)
        break
