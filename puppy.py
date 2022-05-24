a=int(input())
for i in range (a):
    (a,b)=map(int,input().split())
    mx=-float('inf')
    for j in range (1,b+1):
        r=a%j
        if(r>mx):
            mx=r
    print(mx)