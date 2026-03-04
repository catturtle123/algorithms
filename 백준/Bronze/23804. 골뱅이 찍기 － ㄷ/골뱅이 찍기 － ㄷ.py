n = int(input())

# 위
temp = "@@@@@" * n
for i in range(1, n + 1):
    print(temp)

# 중간
temp = "@" * n
temp_n = n * 3
for i in range(temp_n):
    print(temp)

# 밑
temp = "@@@@@" * n
for i in range(1, n + 1):
    print(temp)