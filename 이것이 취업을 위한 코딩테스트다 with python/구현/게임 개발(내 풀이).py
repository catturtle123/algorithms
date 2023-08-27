# 입력 받기
n = input()
nlist = []

# 리스트에 넣기
for i in n:
    nlist.append(i)

nlist.sort()

result = 0

# 숫자면 더하고 아니면 출력
for i in nlist:
    if str(i).isdigit():
        result += int(i)
    else:
        print(i,end="")

# result 값이 0이 아니라면 출력
if result != 0:
    print(result)

# 아쉬웠던 점 : 처음 리스트에 넣을 때 숫자 분류를 했으면 for 문을 한 번 더 안 써도 됐었음.
