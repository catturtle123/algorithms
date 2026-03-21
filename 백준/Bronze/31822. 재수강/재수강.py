s = input()
s = s[:5]

n = int(input())
result = 0  
for _ in range(n):
    s2 = input()
    s2 = s2[:5]
    
    if s == s2:
        result += 1

print(result)