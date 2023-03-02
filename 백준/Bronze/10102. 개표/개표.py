n = int(input())
s = input()

A = s.count("A")
B = s.count("B")

if A==B:
    print("Tie")
elif A>B:
    print("A")
else:
    print("B")