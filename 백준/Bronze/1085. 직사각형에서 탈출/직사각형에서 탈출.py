x,y,w,h = map(int,input().split())

xr = w - x
xl = x

yu = h-y
yd = y

dlist = [xr,xl,yu,yd]

dlist.sort()

print(dlist[0])
