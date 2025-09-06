s = input()

zeroNum = 0
oneNum = 0
current = s[0]
if current == '1':
    oneNum += 1
else:
    zeroNum += 1

for i in s[1:]:
    if current == '0' and i == '1':
        oneNum += 1
        current = '1'
    elif current == '1' and i == '0':
        zeroNum += 1
        current = '0'

result = min(zeroNum, oneNum)

print(result)