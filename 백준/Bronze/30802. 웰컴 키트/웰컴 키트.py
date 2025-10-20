# 웰컴 키트로 티셔츠 한장과 펜 한자루를 나누어줄 예정

# 조건
# 티셔츠는 S, M, L, XL, XXL, XXXL 6가지 사이즈 존재 같은 사이즈를 T장 묶음 만큼 주문 가능
# 펜은 한자루 혹은 P 자루씩 묶음으로 주문 가능
# 티셔츠는 남아도 됨.

# 티셔츠를 T장씩 최소 몇 묶음을 주문해야하는 지 
# 펜을 P자루씩 최대 몇 묶음 주문할 수 있고, 그 때 펜을 한 자루씩 몇 개 주문

import sys
import math
input = sys.stdin.readline

n = int(input())

tlist = list(map(int, input().split()))

t, p = map(int, input().split())

t_num = 0
for i in tlist:
    t_num += math.ceil(i / t)

p_list_num = n // p
p_num = n % p

print(t_num)
print(p_list_num, p_num)