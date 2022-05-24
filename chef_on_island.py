a=int(input())
for i in range (a):
    (x,y,xr,yr,D)=map(int,input().split())
    f=x/xr
    w=y/yr
    b=min(f,w)
    if(b>=D):
        print("YES")
    else:
        print("NO")