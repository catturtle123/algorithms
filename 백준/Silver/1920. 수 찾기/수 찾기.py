import sys
input = sys.stdin.readline

def binary_search(nlist, x):
    start = 0
    end = len(nlist) - 1

    while start <= end:
        mid = (start + end) // 2

        if nlist[mid] == x:
            return True
        elif nlist[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    
    return False

n = int(input())
nlist = list(map(int, input().split()))

m = int(input())
mlist = list(map(int, input().split())) # 여기 숫자 중 nlist에 존재하면 1 아니면 0

nlist.sort()
for i in mlist:
    if binary_search(nlist, i):
        print(1)
    else:
        print(0)