# 정해진 총액 이하에서 가능한 최대의 총예산을 아래와 같은 방법으로 배정
# 1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 배정
# 2. 아니라면, 특정한 정수 상한액을 계산하여 모두 상한액을 배정, 상한액 이하면 그대로 배정
# 입력, 지방의 수, 예산, 총액

import sys
input = sys.stdin.readline

def binary_search(nlist, x):
    start = 0
    end = nlist[-1]

    while start <= end:
        mid = (start + end) // 2

        # 가운데 값을 기준으로 낮은 값들은 그대로 더하고 나머지는 mid 값으로 모두를 더함
        temp = 0
        for i in range(len(nlist)):
            if nlist[i] > mid:
                temp = sum(nlist[:i]) + (mid * len(nlist[i:]))
                break
        
        if temp == x:
            return mid
        elif temp < x:
            # 해당 값이 x보다 낮거나 같다면 start = mid + 1
            start = mid + 1
        else:
            # 해당 값이 x보다 높다면 end = mid - 1
            end = mid - 1
    
    return end

n = int(input())
nlist = list(map(int, input().split()))
max_num = int(input())

nlist.sort()
result = binary_search(nlist, max_num)
print(result)

# 완전히 같다는 뜻은? -> 최대 상한치를 다 썻다는 뜻 -> 가장 최대라는 뜻