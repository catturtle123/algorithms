n = int(input())

s = 100000000
result = pow(n, 2)

if result <= s:
    print("Accepted")
else:
    print("Time limit exceeded")