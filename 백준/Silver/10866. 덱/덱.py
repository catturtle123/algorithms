import sys
n = int(input())

nlist = []
for i in range(n):
    s = sys.stdin.readline().strip()

    if s.find("push_front") != -1:
        p = s.find(" ")
        value = s[p:].strip()
        nlist.insert(0,value)
    elif s.find("push_back") != -1:
        p = s.find(" ")
        value = s[p:].strip()
        nlist.append(value)
    elif s.find("pop_front") != -1:
        if len(nlist) == 0:
            print(-1)
        else:
            print(nlist.pop(0))
    elif s.find("pop_back") != -1:
        if len(nlist) == 0:
            print(-1)
        else:
            print(nlist.pop())
    elif s.find("size") != -1:
        print(len(nlist))
    elif s.find("empty") != -1:
        if len(nlist) == 0:
            print(1)
        else:
            print(0)
    elif s.find("front") != -1:
        if len(nlist) == 0:
            print(-1)
        else:
            print(nlist[0])
    elif s.find("back") != -1:
        if len(nlist) == 0:
            print(-1)
        else:
            print(nlist[-1])