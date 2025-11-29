A, B, V = map(int, input().split())

day = (V - B + (A - B) - 1) // (A - B)

print(day)