import sys
input = sys.stdin.readline

n = int(input())

arr = [0] * n
count = 0
def dfs(depth):
  global count
  if n == depth:
      count += 1
      return
  
  for i in range(n):
      arr[depth] = i
      if check(depth):
          dfs(depth + 1)

def check(current_depth):
  for i in range(current_depth):
      if arr[i] == arr[current_depth] or (abs(arr[i] - arr[current_depth]) == abs(i - current_depth)):
          return False

  return True

dfs(0)
print(count)