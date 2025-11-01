import sys
input = sys.stdin.readline

def check(x):
    for i in nlist:
        if i == x:
            return 1
    
    return 0

def toggle(x):
    if check(x):
        nlist.remove(x)
    else:
        nlist.append(x)

def add(x):
    if not check(x):
        nlist.append(x)

def remove(x):
    if check(x):
        nlist.remove(x)

n = int(input())
nlist = []
for i in range(n):
    a = input().rstrip()

    if a.startswith("all") or a.startswith("empty"):
        oper = a.rstrip()
    else:
        oper, x = a.split()
        x = int(x.rstrip())

    if oper == "add":
        add(x)
    elif oper == "remove":
        remove(x)
    elif oper == "check":
        print(check(x))
    elif oper == "toggle":
        toggle(x)
    elif oper == "all":
        nlist = [i for i in range(1, 21)]
    else:
        nlist.clear()