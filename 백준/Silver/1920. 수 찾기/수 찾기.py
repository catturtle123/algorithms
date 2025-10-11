import sys

def binary_search(li, x):
    start = 0
    end = len(li) - 1

    while start <= end:
        mid = (start + end) // 2

        if li[mid] == x:
            return mid
        elif li[mid] > x:
            end = mid - 1
        else:
           start = mid + 1
    
    return None


input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

nlist.sort()

for i in mlist:
    if binary_search(nlist, i) == None:
      print(0)
    else:
      print(1)