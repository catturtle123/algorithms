n, m = map(int, input().split(' '))
nlist = []

for i in range(n):
    strs = input()
    for j in strs:
        nlist.append(j)

rlist = [[0] for _ in range(n * m)]
pos = [1, -1, m, -m]
for i in range(len(nlist)):
    for j in pos:
        if (0 <= i + j and i + j <= len(nlist) - 1) and nlist[i] == nlist[i + j]:
            if i % m == 0:
                if j != -1:
                    rlist[i].append(i + j + 1)
            elif (i + 1) % m == 0:
                if j != 1:
                    rlist[i].append(i + j + 1)
            else:
                rlist[i].append(i + j + 1)
            

for i in range(len(rlist)):
    rlist[i].pop(0)
    rlist[i].sort()

visited = []

for i in range(n * m):
    visited.append(False)

finish = False
plan = 0
olist = [] # 이미 지나온 경로
slist = [] # 순환된 것
def dfs(here):
    global plan
    global finish
    for i in range(len(rlist[here])):
      if finish:
          break
      there = rlist[here][i]
      if visited[there - 1] == True:
          if sorted((here + 1, there)) not in olist and here + 1 == plan:
              slist.append(here + 1)
              finish = True
          continue
      olist.append(sorted((here + 1, there)))
      visited[there - 1] = True
      dfs(there - 1)



for o in range(n * m):
    plan = o + 1
    visited[o] = True
    dfs(o)
    olist = []
    for j in range(len(visited)):
        visited[j] = False
    if finish:
        print("Yes")
        break

if not finish:
    print("No")