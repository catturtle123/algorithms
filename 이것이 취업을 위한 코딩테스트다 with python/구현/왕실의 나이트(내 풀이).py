# 입력 받기
n = input()

# 위치 설정
p1 = ord(n[0]) - ord("a") + 1
p2 = int(n[-1])

# 나이트의 움직임 설정
np = [(2,1),(2,-1),(1,2),(1,-2),(-2,-1),(-2,1),(-1,-2),(-1,2)]

# 움직이고 난 후 조건 성립 결정
count = 0
for i in np:
    row = i[1]
    col = i[0]
    if p1 + row >= 1 and  p1 + row <= 8 and p2 + col >= 1 and p2 + col <= 8:
        count += 1

# 출력
print(count)
