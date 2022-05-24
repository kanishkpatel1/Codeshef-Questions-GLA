t=int(input())
for i in range(t):
    (M,N,K)=map(int,input().split())
    if((2*K+M)>=N):
        print("YES")
    else:
        print("NO")