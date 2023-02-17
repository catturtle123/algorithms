# 입력받기
n = int(input())
nlist = map(str,input().split())

# 초기값 설정
dx = 1
dy = 1

# 방위마다 판별 후 위치 재설정
for i in nlist:
    if i == "R":
        if dx != n:
            dx += 1
    elif i == "L":
        if dx != 1:
            dx -= 1
    elif i == "U":
        if dy != 1:
            dy -= 1
    else:
        if dy != n:
            dy += 1

# 출력
print(dy,dx)

# 아쉬웠더 점 : 방위 별로 설정하고 그에 따라 대입하는 코드가 더 간결해서 좋았던 것 같다. 행렬로 이루어지는 방위를 잘못 이해하고 y와 x를 반대로 표시하였다.
