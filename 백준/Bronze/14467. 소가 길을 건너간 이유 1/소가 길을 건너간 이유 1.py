n = int(input())
pos = [-1] * 11
count = 0

for _ in range(n):
    cow, location = map(int, input().split())

    if pos[cow] == -1:
        pos[cow] = location
    else:
        if pos[cow] != location:
            count += 1
            pos[cow] = location

print(count)