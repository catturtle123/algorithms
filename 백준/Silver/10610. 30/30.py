s_num = list(map(int, input()))

s_num.sort(reverse=True)

if sum(s_num) % 3 != 0 or s_num[-1] != 0:
    print(-1)
else:
    for i in s_num:
        print(i,end="")