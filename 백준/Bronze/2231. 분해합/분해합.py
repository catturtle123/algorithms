n = int(input())

a = False
for num in range(1, n):
    s = str(num)
    sums = 0
    for i in s:
      sums += int(i)
    
    if sums + num == n:
      print(num)
      a = True
      break

if not a:
   print(0)