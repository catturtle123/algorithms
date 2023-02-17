# 입력받기
n = int(input())

# 카운트 초기화
count = 0

# 시간 하나씩 세기
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) + str(j) + str(k):
                count += 1

# 출력
print(count)
