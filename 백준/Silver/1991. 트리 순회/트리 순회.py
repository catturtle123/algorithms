import sys
input = sys.stdin.readline

def fun(current, setting):

    if setting == 'a': # 전위 순회
        print(chr(current + ord('A') - 1), end="")

        if tree[current][0] != -1:
            fun(tree[current][0], setting)

        if tree[current][1] != -1:
            fun(tree[current][1], setting)
    
    elif setting == 'b': # 중위 순회
        if tree[current][0] != -1:
            fun(tree[current][0], setting)
        
        print(chr(current + ord('A') - 1), end="")

        if tree[current][1] != -1:
            fun(tree[current][1], setting)
    
    elif setting == 'c': # 후위 순회
        if tree[current][0] != -1:
            fun(tree[current][0], setting)

        if tree[current][1] != -1:
            fun(tree[current][1], setting)
        
        print(chr(current + ord('A') - 1), end="")

n = int(input())
tree = [[] for _ in range(n + 1)]

for i in range(n):
    a, b, c = map(str, input().split())

    a = ord(a) - ord('A') + 1
    b = ord(b) - ord('A') + 1
    c = ord(c) - ord('A') + 1

    if b < 0:
        b = -1
    
    if c < 0:
        c = -1
    
    tree[a].append(b)
    tree[a].append(c)

fun(1, "a")
print()
fun(1, "b")
print()
fun(1, "c")