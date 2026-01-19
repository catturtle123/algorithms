import sys
input = sys.stdin.readline

def solve(idx):
    if idx == len(zeros):
        return True

    y, x = zeros[idx]

    for num in range(1, 10):
        if is_possible(y, x, num):
            nlist[y][x] = num

            if solve(idx + 1):
                return True
            
            nlist[y][x] = 0
    
    return False

def is_possible(y, x, num):
    for i in range(9):
        if nlist[y][i] == num or nlist[i][x] == num:
            return False
    
    starty, startx = (y // 3) * 3, (x // 3) * 3
    for i in range(3):
        for j in range(3):
            if nlist[starty + i][startx + j] == num:
                return False
    
    return True

nlist = []
for _ in range(9):
    n = list(map(int, input().split()))
    nlist.append(n)

zeros = []
for i in range(9):
    for j in range(9):
        if nlist[i][j] == 0:
            zeros.append((i, j))


solve(0)

for i in range(9):
    for j in range(9):
        print(nlist[i][j], end=" ")
    print()