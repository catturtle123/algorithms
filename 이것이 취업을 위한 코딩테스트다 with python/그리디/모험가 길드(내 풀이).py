# 입력 받기
n = int(input())
# 입력 받기 2
nlist = list(map(int,input().split()))

# 정렬 시키기
nlist.sort()

# 사용할 변수 초기화
count1 = 0
count2 = 0

# 모든 데이터 반복
for i in nlist:
    # 사람 수 마다 올리기
    count1 += 1
    if count1 >= i:
        # 그룹이 결성되면 결과값 상승
        count2 += 1
        count1 = 0

# 답 출력
print(count2)
