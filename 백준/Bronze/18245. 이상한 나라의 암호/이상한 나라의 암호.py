import sys

count = 2
while True:
    n = sys.stdin.readline().rstrip()  
    if n == "Was it a cat I saw?":
        break
    for i in range(0,len(n),count):
        print(n[i],end="")
    count += 1
    print()