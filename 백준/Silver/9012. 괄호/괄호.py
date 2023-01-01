n = int(input())



for i in range(n):
        nlist = []
        ulist = 0
        string = input()

        for j in string:
                nlist.append(j)

        for o in nlist:
                if o == "(":
                        ulist += 1
                elif o == ")":
                        if ulist == 0:
                                ulist = -1
                                break
                        ulist -= 1

        if nlist[-1] == ")" and ulist == 0:
                print("YES")
        else:
                print("NO")