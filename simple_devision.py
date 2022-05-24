t=int(input())
for i in range(t):
    suma=0
    (n,x,y)=map(int,input().split())
    a=list(map(int,input().split()))
    for i in a:
        if((i<=x) and (i%y==0)):
            suma+=1
    print(suma)