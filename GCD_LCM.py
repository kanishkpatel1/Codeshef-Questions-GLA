n=int(input())
for  i in range (n):
    (a,b)=map(int,input().split())
    x,y=a,b
    while(b!=0):
        t=b
        b=a%b
        a=t
    gcd=a
    lcm=(x*y)//gcd
    print(gcd," ",lcm)