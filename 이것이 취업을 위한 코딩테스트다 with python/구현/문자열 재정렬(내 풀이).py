# 입력 받기
n = input()
slist = []
nlist = []

# 숫자, 문자 구별하기
for i in n:
    if i.isdigit():
        nlist.append(i)
    else:
        slist.append(i)

# 정렬 시키기
slist.sort()

# 문자열 출력
for i in slist:
    print(i,end="")

# 숫자 합 출력
sum = 0
for i in nlist:
    sum += int(i)
print(sum)
