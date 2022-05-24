n=int(input())
a=b=t=0
for i in range(n):
    (x,m,d)=map(int,input().split())
    a,b=x*m,x+b
    t=min(a,b)
    print(t)