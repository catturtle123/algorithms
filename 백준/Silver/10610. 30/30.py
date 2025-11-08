n = list(input())

def is_thrity():
    is_zero = False
    sums = 0
    for i in n:
        if i == '0':
            is_zero = True
        sums += int(i)

    if not is_zero:
        print(-1)
        return False

    if sums % 3 != 0:
        print(-1)
        return False

    return True

if is_thrity():
    n.sort(reverse=True)
    for i in n:
        print(i, end="")