import sys
input = sys.stdin.readline

def binary_search(nlist, x):
    start = 0
    end = nlist[-1]

    while start <= end:
        mid = (start + end) // 2

        temp = 0
        for i in range(len(nlist)):
            if nlist[i] > mid:
                temp = sum(nlist[:i]) + (len(nlist[i:]) * mid)
                break

        if temp <= x:
            start = mid + 1
        else:
            end = mid - 1

    return end

n = int(input())
nlist = list(map(int, input().split()))
max_num = int(input())
nlist.sort()
print(binary_search(nlist, max_num))