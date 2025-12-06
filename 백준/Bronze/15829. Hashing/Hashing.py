n = int(input())
s = input()
slist = list(s)

sum = 0
for i in range(len(slist)):
    temp = ord(slist[i]) - ord('a') + 1
    sum += (temp * pow(31, i))

print(sum % 1234567891)