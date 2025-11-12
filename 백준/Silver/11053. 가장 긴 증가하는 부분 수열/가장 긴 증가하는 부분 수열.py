import bisect
n = int(input())
nlist = list(map(int, input().split()))

def lis(nlist):
    result = []
    for i in nlist:
        pos = bisect.bisect_left(result, i)
        if pos == len(result):
            result.append(i)
        else:
            result[pos] = i

    return result

print(len(lis(nlist)))