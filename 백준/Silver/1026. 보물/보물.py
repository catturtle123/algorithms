import sys

n = int(input())

upList = []
upList = list(map(int,sys.stdin.readline().strip().split()))

downList = []
downList = list(map(int,sys.stdin.readline().strip().split()))

upList.sort()
downList.sort()
downList.reverse()

sum = 0
for i in range(n):
    sum += (upList[i]*downList[i])

print(sum)