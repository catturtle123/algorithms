nlist = [[" "]*15 for i in range(5)]
olist = []

for i in range(5):
    s = input()
    n = len(s)
    olist.append(n)
    for k in range(n):
        nlist[i][k] = s[k]

for i in range(max(olist)):
    for j in range(5):
        if nlist[j][i] != " ":
            print(nlist[j][i],end="")
   