s = input()
n = int(input())

count = 0
for i in range(n):
    s2 = input()
    if s2 == s:
        count += 1
    
print(count)