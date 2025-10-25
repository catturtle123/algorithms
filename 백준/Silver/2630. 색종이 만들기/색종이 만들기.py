import sys
input = sys.stdin.readline

n = int(input())
maps = []

for i in range(n):
    maps.append(list(map(int, input().split())))

blue = 0
white = 0
def divide(y, x, size):
    global blue
    global white

    color = maps[y][x]

    for i in range(y, y + size):
        for j in range(x, x + size):
            if color != maps[i][j]:
                divide(y, x, size // 2)
                divide(y + size // 2, x, size // 2)
                divide(y, x + size // 2, size // 2)
                divide(y + size // 2, x + size // 2, size // 2)
                return
    
    if color == 1:
        blue += 1
    else:
        white += 1

divide(0,0,n)
print(white)
print(blue)