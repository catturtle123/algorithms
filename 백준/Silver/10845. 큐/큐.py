import sys
n = int(input())


nlist = []
for i in range(n):
    answer = sys.stdin.readline().strip()
    if answer.find("push") == 0:
        p = answer.find(" ")
        nlist.append(answer[p:].strip())
    elif answer.find("pop") == 0:
        if len(nlist) == 0:
            print(-1)
        else:
            u = nlist.pop(0)
            print(u)
    elif answer.find("size") == 0:
        print(len(nlist))
    elif answer.find("empty") == 0:
        if len(nlist) == 0:
            print(1)
        else:
            print(0)
    elif answer.find("front") == 0:
        if len(nlist) == 0:
            print(-1)
        else:
            print(nlist[0])
    elif answer.find("back") == 0:
        if len(nlist) == 0:
            print(-1)
        else:
            print(nlist[-1])
