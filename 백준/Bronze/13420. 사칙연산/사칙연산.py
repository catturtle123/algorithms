n = int(input())

for _ in range(n):
    s_list = list(map(str, input().split()))

    result = 0
    if s_list[1] == "+":
        result = int(s_list[0]) + int(s_list[2])
    elif s_list[1] == "-":
        result = int(s_list[0]) - int(s_list[2])
    elif s_list[1] == "/":
        result = int(s_list[0]) / int(s_list[2])
    elif s_list[1] == "*":
        result = int(s_list[0]) * int(s_list[2])
    
    if int(s_list[4]) == result:
        print("correct")
    else:
        print("wrong answer")