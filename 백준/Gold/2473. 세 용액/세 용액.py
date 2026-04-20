import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = sys.maxsize
answer = []

for i in range(n - 2):
    left = i + 1
    right = n - 1

    while left < right:
        total = arr[i] + arr[left] + arr[right]

        if abs(total) < result:
            result = abs(total)
            answer = [arr[i], arr[left], arr[right]]

        if total > 0:
            right -= 1
        elif total < 0:
            left += 1
        else:
            print(*answer)
            exit(0)

print(*answer)