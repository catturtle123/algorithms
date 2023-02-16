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

# 아쉬웠던 점 : 초반 접근법이 다소 달라서 시간이 많이 걸렸다. 문제를 많이 접해보며 접근 방법에 대한 감각을 더욱 키워야 겠다.
