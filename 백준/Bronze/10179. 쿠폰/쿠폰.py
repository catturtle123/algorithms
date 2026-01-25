n = int(input())

for _ in range(n):
    r = float(input())
    result = r - (r * 0.2)
    print("${:.2f}".format(result))