n = int(input())

for _ in range(n):
    e = int(input())
    e_list = list(map(int, input().split()))
    print(sum(e_list))