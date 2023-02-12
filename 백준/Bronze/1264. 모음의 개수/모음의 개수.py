while True:
    count = 0
    n = input()
    if n == "#":
        break
    for i in n:
        count += i.count("a")
        count += i.count("e")
        count += i.count("i")
        count += i.count("o")
        count += i.count("u")
        count += i.count("A")
        count += i.count("E")
        count += i.count("I")
        count += i.count("O")
        count += i.count("U")
    print(count)