import sys
input = sys.stdin.readline

def prev_function(target):
    prev = target[0]
    prev_list = []

    for i in range(1, len(target)):
        if prev != target[i]:
            if target[i] in prev_list:
                return False
            else:
                prev_list.append(prev)
                prev = target[i]
    
    return True
    

count = 0
n = int(input())
for i in range(n):
    s = input().rstrip()
    if prev_function(s):
        count += 1

print(count)