import sys
input = sys.stdin.readline

def binary_search(nlist, x):
    start = 0
    end = nlist[-1]

    while start <= end:
        mid = (start + end) // 2

        temp = 0
        for i in nlist:
            if i > mid:
                temp += (i - mid)
        
        if temp >= x:
            start = mid + 1
        else:
            end = mid - 1
    
    return end



n, m = map(int, input().split())
nlist = list(map(int, input().split()))

nlist.sort()
print(binary_search(nlist, m))