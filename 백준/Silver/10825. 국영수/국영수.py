import sys

input = sys.stdin.readline

n = int(input())

nlist = []
for i in range(n):
    name, n1, n2, n3 = input().split(" ")
    nlist.append((name, int(n1), int(n2), int(n3)))

# 국어 점수가 감소
# 영어 점수가 증가하는
# 수학 점수가 감소하는
# 사전 순으로 중가하는 순서대로

def map_sort(list):
    return -list[1], list[2], -list[3], list[0]

nlist = sorted(nlist, key=map_sort)

for i in range(n):
    print(nlist[i][0])