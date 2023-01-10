import sys
n1,n2 = map(int,input().split())

one = set()
three = {}
for i in range(n1):
    a,b = map(str,sys.stdin.readline().split())
    one.add(a.strip())
    three[a.strip()] = b.strip()

for i in range(n2):
    n = sys.stdin.readline().strip()
    print(three[n])

