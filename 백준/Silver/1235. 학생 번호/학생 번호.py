import sys
input = sys.stdin.readline

n = int(input())

nlist = []
for _ in range(n):
    s = input().rstrip()
    nlist.append(s)

result = sys.maxsize
length = len(s)
for i in range(length):
    for j in range(n):
        nlist[j] = nlist[j][1:]
    
    is_break = False
    for j in range(n):
        if nlist[j] in nlist[j + 1:]:
            is_break = True
            break
    
    if not is_break:
        result = min(result, len(nlist[0]))

if result == sys.maxsize:
    print(length)
else:
    print(result)