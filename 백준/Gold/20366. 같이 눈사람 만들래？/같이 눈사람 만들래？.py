import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
nlist.sort()

answer = sys.maxsize

for i in range(n):
    for j in range(i + 3, n):
        target = nlist[i] + nlist[j]

        left = i + 1
        right = j - 1

        while left < right:
            snowman_height = nlist[left] + nlist[right]
            cost = abs(target - snowman_height)

            if cost < answer:
                answer = cost

            if answer == 0:
                print(0)
                exit(0)

            if snowman_height < target:
                left += 1
            else:
                right -= 1

print(answer)