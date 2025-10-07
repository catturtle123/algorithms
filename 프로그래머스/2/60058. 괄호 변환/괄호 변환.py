def isCorrect(w):
    count = 0
    for i in w:
        if i == "(":
            count += 1
        else:
            count  -= 1
        
        if count < 0:
            return False
    
    if count == 0:
        return True
    else:
        return False

def dfs(w):
    # 1단계
    if w == "":
        return ""
    
    count = 0
    u = ""
    v = ""
    for i in range(len(w)):
        if w[i] == "(":
            count += 1
        else:
            count -= 1
        
        if count == 0:
            u = w[:i + 1]
            v = w[i + 1:]
            break
    
    if u == "":
        u = w
        v = ""

    if isCorrect(u):
        u += dfs(v)
        return u
    else:
        temp = "("
        temp += dfs(v)
        temp += ")"
        u = u[1:-1]
        
        temp2 = ""
        for i in u:
            if i == "(":
                temp2 += ")"
            else:
                temp2 += "("
        
        temp += temp2

        return temp

def solution(p):
    answer = dfs(p)
    
    return answer