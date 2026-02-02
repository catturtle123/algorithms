n = int(input())
s = input()

# 상근
a = ["A","B","C"]
a_name = "Adrian"
a_result = 0

# 창영
b = ["B","A","B","C"]
b_name = "Bruno"
b_result = 0

# 현진
c = ["C","C","A","A","B","B"]
c_name = "Goran"
c_result = 0

for i in range(len(s)):
    if a[i % 3] == s[i]:
        a_result += 1

    if b[i % 4] == s[i]:
        b_result += 1
    
    if c[i % 6] == s[i]:
        c_result += 1

result = max(a_result, b_result, c_result)
print(result)
if a_result == result:
    print(a_name)

if b_result == result:
    print(b_name)

if c_result == result:
    print(c_name)