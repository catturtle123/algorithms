import sys

while True:
    u = 0
    n = int(sys.stdin.readline().strip())
    n = str(n)
    if n == "0":
        break
    for i in range(len(n)//2):
        if n[i] != n[len(n)-1-i]:
            u += 1
    if u >= 1:
        print("no")
    else:
        print("yes")
    