import sys
input = sys.stdin.readline

time = int(input())

def bell_ford(start):
  values[start] = 0

  for i in range(n):
    for j in range(len(graph)):
      sv, ev, ec = graph[j]
      if values[sv] + ec < values[ev]:
        values[ev] = values[sv] + ec

        if i == n - 1:
          return False
  
  return True

INF = sys.maxsize

for t in range(time):
  n, m, w = map(int, input().split())

  graph = []
  for i in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))
    graph.append((b, a, c))
    
  
  for i in range(w):
    a, b, c = map(int, input().split())
    graph.append((a, b, -c))

  values = [INF] * (n + 1)

  if bell_ford(1):
    print("NO")
  else:
    print("YES")