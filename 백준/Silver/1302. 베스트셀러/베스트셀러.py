import sys

input = sys.stdin.readline

def sort_def(list):
    return -list[1], list[0]

n = int(input())

a = {}

for i in range(n):
    b = input().rstrip()

    if b in a.keys():
        a[b] += 1
    else:
        a[b] = 1

c = sorted(a.items(), key=sort_def)

print(c[0][0])