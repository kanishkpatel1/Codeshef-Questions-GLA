t=int(input())
for i in range(t):
    (n,x,p)=map(int,input().split())
    nc=n-x
    nu=3*x-nc
    if(nu>=p):
        print("PASS")
    else:
        print("FAIL")