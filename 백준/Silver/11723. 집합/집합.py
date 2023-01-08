import sys

n = int(input())


nlist = set()

for i in range(n):
    n = sys.stdin.readline().strip()

    if n.find("add") != -1:
        p = n.find(" ")
        num = int(n[p:])
        if num in nlist:
            pass
        else:
            nlist.add(num)
    elif n.find("remove") != -1:
        p = n.find(" ")
        num = int(n[p:])
        if num in nlist:
            nlist.remove(num)
    elif n.find("check") != -1:
        p = n.find(" ")
        num = int(n[p:])
        if num in nlist:
            print(1)
        else:
            print(0)
    elif n.find("all") != -1:
        nlist = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif n.find("empty") != -1:
        nlist.clear()
    elif n.find("toggle") != -1:
        p = n.find(" ")
        num = int(n[p:])
        if num in nlist:
            nlist.remove(num)
        else:
            nlist.add(num)