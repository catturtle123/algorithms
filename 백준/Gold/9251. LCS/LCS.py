s1 = list(input())
s2 = list(input())

slist = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

for i in range(1, len(s2) + 1):
    for j in range(1, len(s1) + 1):
        if s2[i - 1] == s1[j - 1]:
            slist[i][j] = slist[i - 1][j - 1] + 1
        else:
            slist[i][j] = max(slist[i - 1][j], slist[i][j - 1])

print(slist[len(s2)][len(s1)])
