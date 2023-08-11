n = int(input())
n = 1000 - n
coin = 0
array = [500,100,50,10,5,1]

for i in array:
    coin += n // i
    n %= i

print(coin)