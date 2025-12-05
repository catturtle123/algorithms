s = input()

pri = {
    "+" : 1,
    "-" : 1,
    "*" : 2,
    "/" : 2,
}

stack = []
result = []

for i in s:
    if 'A' <= i <= 'Z':
        result.append(i)
    elif i == "(":
        stack.append(i)
    elif i == ")":
        while stack and stack[-1] != "(":
            result.append(stack.pop())
        stack.pop()
    else:
        while stack and stack[-1] != "(" and pri[stack[-1]] >= pri[i]:
            result.append(stack.pop())
        stack.append(i)

while stack:
    result.append(stack.pop())

for i in result:
    print(i, end="")