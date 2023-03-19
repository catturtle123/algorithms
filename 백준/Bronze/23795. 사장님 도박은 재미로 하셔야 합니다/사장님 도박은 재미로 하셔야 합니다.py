import sys

n = 0
sum = 0
while n != -1:
    sum += n
    n = int(sys.stdin.readline().rstrip())
    
print(sum)