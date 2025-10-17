import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())
Clist = list(map(str, input().split()))

result = []
for comb in combinations(Clist, L):
    is_a = False
    is_l = False

    count = 0
    s = []
    for i in comb:
        if i in "aeiou":
            is_a = True
        else:
            count += 1
        
        if count == 2:
            is_l = True
        
        s.append(i)
    
    if is_a and is_l:
        s.sort()
        st = ""
        for i in s:
            st += i
        
        result.append(st)

result.sort()  
for i in result:
    print(i)