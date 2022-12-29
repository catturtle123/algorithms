import sys

n = int(sys.stdin.readline().strip())

nlist = []
for i in range(n):
    n = sys.stdin.readline().strip()
    
    if n.find("push") == 0:
        p = n.find(" ")
        nlist.append(n[p:].strip())
    elif n.find("pop") == 0:
        if len(nlist) == 0:
            print(-1)   
        else:
            print(nlist[-1])
            nlist.pop()
    elif n.find("size") == 0:
        print(len(nlist))
    elif n.find("empty") == 0:
        if len(nlist) == 0:
            print(1)
        else:
            print(0)
    elif n.find("top") == 0:
        if len(nlist) == 0:
            print(-1)
        else:
            print(nlist[-1])