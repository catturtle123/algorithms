t = int(input())

for case in range(1, t + 1):
    s = input()
    count = [0] * 26

    for ch in s:
        if ch.isalpha():
            ch = ch.lower()
            count[ord(ch) - ord('a')] += 1

    mn = min(count)

    if mn == 0:
        result = "Not a pangram"
    elif mn == 1:
        result = "Pangram!"
    elif mn == 2:
        result = "Double pangram!!"
    else:
        result = "Triple pangram!!!"

    print(f"Case {case}: {result}")