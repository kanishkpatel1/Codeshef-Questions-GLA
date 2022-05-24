t=int(input())
for i in range(t):
    (n,s)=map(int,input().split())
    pos=(n*(n+1)//2)-s
    if(pos<=n and pos>=1):
        print(pos)
    else:
        print("-1")