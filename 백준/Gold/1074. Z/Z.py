n, r, c = map(int, input().split())

def z(y, x, n, length):
    if n == 0:
        print(length)
        return length

    div = pow(2, n - 1)
    if r < y + div and c < x + div: # 1 사분면
        z(y, x, n - 1, length)

    elif r < y + div and c >= x + div: # 2 사분면
        z(y, x + div, n - 1, length + div * div)

    elif r >= y + div and c < x + div: # 3 사분면
        z(y + div, x, n - 1, length + 2 * div * div)

    elif r >= y + div and c >= x + div: # 4 사분면
        z(y + div, x + div, n - 1, length + 3 * div * div)

z(0, 0, n, 0)