# 등호 하나와 더하기, 빼기, 곱하기, 나누기 기호

n1, n2, n3 = map(int, input().split())

if n1 + n2 == n3:
    print(f"{n1}+{n2}={n3}")

elif n1 - n2 == n3:
    print(f"{n1}-{n2}={n3}")

elif n1 * n2 == n3:
    print(f"{n1}*{n2}={n3}")

elif n1 / n2 == n3:
    print(f"{n1}/{n2}={n3}")

elif n1 == n2 + n3:
    print(f"{n1}={n2}+{n3}")

elif n1 == n2 * n3:
    print(f"{n1}={n2}*{n3}")

elif n1 == n2 - n3:
    print(f"{n1}={n2}-{n3}")

elif n1 == n2 / n3:
    print(f"{n1}={n2}/{n3}")