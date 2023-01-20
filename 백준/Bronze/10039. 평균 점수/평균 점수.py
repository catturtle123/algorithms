sum = 0
for i in range(5):
    score = int(input())
    if score < 40:
        score = 40
    sum += score
    
sum = sum / 5
print(int(sum))