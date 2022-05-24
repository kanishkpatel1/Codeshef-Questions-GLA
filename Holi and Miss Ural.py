
t=int(input())
for i in range(t):
    lst=[]
    (n,k)=map(int,input().split())
    d=list(map(int,input().split()))
    r=list(map(int,input().split()))
    for j in range(n):
        a=k*d[j]+r[j]
        lst.append(a)
    print(min(lst))