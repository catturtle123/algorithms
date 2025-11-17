import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())

    nlist = []
    for j in range(2):
        nlist.append(list(map(int, input().split())))
    
    score = [[0] * n for _ in range(2)]
    score[0][0] = nlist[0][0]
    score[1][0] = nlist[1][0]

    if n > 1:
        score[0][1] = nlist[1][0] + nlist[0][1]
        score[1][1] = nlist[0][0] + nlist[1][1]

        for j in range(2, n):
            for o in range(2):
                if o == 0:
                    score[o][j] = max(nlist[o][j] + score[o + 1][j - 1], nlist[o][j] + score[o][j - 2], nlist[o][j] + score[o + 1][j - 2])
                else:
                    score[o][j] = max(nlist[o][j] + score[o - 1][j - 1], nlist[o][j] + score[o][j - 2], nlist[o][j] + score[o - 1][j - 2])

        print(max(score[0][n - 1], score[1][n - 1], score[0][n - 2], score[1][n - 2]))
    else:
        print(max(score[0][0], score[1][0]))