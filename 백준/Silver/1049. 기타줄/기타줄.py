# 기타줄 N개가 끊어짐
# 새로운 줄을 사거나 교체해야함
# 6줄 패키지, 낱개도 가능
# 끊어진 기타줄(N), 기타줄 브랜드(M)

# 브루트포스
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

brands_other = []
brands_package = []
for i in range(m):
    a, b = map(int, input().split())
    brands_package.append(a)
    brands_package.append(b * 6)

    brands_other.append(a)
    brands_other.append(b * (n % 6))

min_brand_package = min(brands_package)
min_brand_other = min(brands_other)

print(((n // 6) * min_brand_package) + (min_brand_other))