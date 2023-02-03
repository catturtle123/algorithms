count = 0
count2 = 0

for i in range(8):    
    n = input()
    
    if count2 == 0:
        for i in range(0,len(n),2):
            if n[i] == "F":
                count += 1
        count2 = 1
    elif count2 == 1:        
        for i in range(1,len(n),2):
            if n[i] == "F":
                count += 1
        count2 = 0
        


print(count)