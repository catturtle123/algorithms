s = list(map(str, input().split()))

while not (s[0] == "#" and s[1] == "0" and s[2] == "0"):
    if int(s[1]) > 17 or int(s[2]) >= 80:
        print(s[0] + " Senior")
    else:
        print(s[0] + " Junior")
    
    s = list(map(str, input().split()))