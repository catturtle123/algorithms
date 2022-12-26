n,m,k = map(int,input().split()) # 나누어서 입력 받아서 변수로 저장한다.
u = 0

numList = list(map(int,input().split())) # 나누어서 입력 받아서 리스트로 저장한다.

for i in range(len(numList)-1,0,-1): # bubbleSort로 정렬한다.
    for j in range(i):
        if numList[j] > numList[j+1]:
            numList[j], numList[j+1] = numList[j+1],numList[j]

sum = 0 # 합계를 설정한다.

while u < m:
    for i in range(k): # 가장 큰 숫자를 횟수만큼 더한다.
        sum += numList[len(numList)-1]
        u += 1
    
    sum += numList[len(numList)-2] # 반복 제한이 있기에 두번째로 큰 수를 더해준다.
    u += 1
    
print(sum) # 합계를 출력한다.

# 아쉬웠던 점 : 파이썬의 내장함수인 sort함수를 문제를 풀때 생각하지 못했다, 규칙을 파악하여 더 빠르게 풀수 있었으나 생각을 해내지 못했다.
