import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def make_tree(currentNode, parent):
    for node in graph[currentNode]:
        if node != parent:
            child[currentNode].append(node)
            # currentNode = node
            make_tree(node, currentNode)

def countSubTreeNodes(currentNode):
    size[currentNode] = 1
    for node in child[currentNode]:
        countSubTreeNodes(node)
        size[currentNode] += size[node]

n, r, q = map(int, input().split())

size = [0] * (n + 1)
child = [[] for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

make_tree(r, -1)
countSubTreeNodes(r)

for _ in range(q):
    f = int(input())
    print(size[f])