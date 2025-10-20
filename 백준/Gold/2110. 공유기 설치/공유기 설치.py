import sys
input = sys.stdin.readline


n, c = map(int, input().split())

nlist = []
for i in range(n):
    a = int(input())
    nlist.append(a)

nlist.sort()

start = 1
end = nlist[-1] - nlist[0]

result = 0
while start <= end:
    mid = (start + end) // 2

    count = 1
    last = nlist[0]
    for i in nlist[1:]:
        if i - last >= mid:
            count += 1
            last = i
        
    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)