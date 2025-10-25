import sys
input = sys.stdin.readline

def binary_search(start, end):
    result = 0
    while start <= end: 
        mid = (start + end) // 2

        sums = 0
        for i in nlist:
            temp = i - mid
            if temp > 0:
                sums += temp

        if sums >= m:
            result = mid   
            start = mid + 1
        else:
            end = mid - 1

    print(result)  

n, m = map(int, input().split())
nlist = list(map(int, input().split()))

start = 0
end = max(nlist)
binary_search(start, end)
