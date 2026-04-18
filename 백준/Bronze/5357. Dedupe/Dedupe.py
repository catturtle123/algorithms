n = int(input())
for _ in range(n):
    s = input()
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            print(s[i - 1], end="")
    
    print(s[len(s) - 1])
        