import sys
n = int(sys.stdin.readline().strip())

s1 = sys.stdin.readline().strip()
for i in range(n-1):
    u = ""
    s2 = sys.stdin.readline().strip()

    for j in range(len(s1)):
        if s1[j] != s2[j]:
            u += "?"
        else:
            u += s1[j]
        
    
    s1 = u

print(s1)
