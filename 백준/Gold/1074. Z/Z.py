import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

def divide_conquer(y, x, n, length):
    if n == 1:
        print(length)
        return
    
    half = n // 2

    if r < y + half and c < x + half:
        divide_conquer(y, x, half, length)
    elif r < y + half and c >= x + half:
        divide_conquer(y, x + half, half, length + half * half)
    elif r >= y + half and c < x + half:
        divide_conquer(y + half, x, half, length + 2 * half * half)
    else:
        divide_conquer(y + half, x + half, half, length + 3 * half * half)

N = 2 ** N
divide_conquer(0, 0, N, 0)