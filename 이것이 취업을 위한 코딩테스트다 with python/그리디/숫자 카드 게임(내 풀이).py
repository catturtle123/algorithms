a,b = map(int,input().split())

ulist = []
nlist = []
for i in range(a): # a*b만큼 숫자 받기
    ulist = list(map(int,input().split()))
    nlist += ulist

ulist = []
l = 0
p = 0
rlist = []
for u in range(a):
    ulist = []
    min_int = 10001
    for i in range(u*b,b*(u+1)): # 한 줄씩 찾아내기
        ulist.append(nlist[i])
    for j in ulist:
        if min_int > j: # 최솟값 찾기
            min_int = j
    rlist.append(min_int) # 최솟값 모아놓기

rlist.sort()
    

print(rlist[-1]) # 가장 큰 수 프린트

# 아쉬웠던 점 : min, max함수를 생각해내지 못했다.
