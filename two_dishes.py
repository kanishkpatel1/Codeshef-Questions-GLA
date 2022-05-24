t=int(input())
for i in range(t):
    (n,s)=map(int,input().split())
    if(s<=n):
        d=s
    else:
        d=2*n-s
    print(d)
