n = int(input())

count = 0
for i in range(n):
    o = ""
    s = input()
    for i in s:
        if i.isnumeric():
            o += i
    
    o = int(o)
    if o <= 90:
        count += 1

print(count)