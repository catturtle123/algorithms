n = input()
mid = len(n) // 2

nlist1 = list(map(int, n[:mid]))
nlist2 = list(map(int, n[mid:]))

if sum(nlist1) == sum(nlist2):
    print("LUCKY")
else:
    print("READY")