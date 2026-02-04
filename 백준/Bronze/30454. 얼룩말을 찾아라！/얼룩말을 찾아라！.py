n, m = map(int, input().split())

result_list = [0] * n
for j in range(n):
    s = input()
    a = s.split("0")
    
    for i in a:
        if "1" in i:
            result_list[j] += 1
    
maxs = max(result_list)
print(maxs, result_list.count(maxs))