a, b = map(int, input().split())
c, d = map(int, input().split())

result1 = a/c + b/d
result2 = c/d + a/b
result3 = d/b + c/a
result4 = b/a + d/c

result = max(result1, result2, result3, result4)

if result1 == result:
    print(0)
elif result2 == result:
    print(1)
elif result3 == result:
    print(2)
elif result4 == result:
    print(3)