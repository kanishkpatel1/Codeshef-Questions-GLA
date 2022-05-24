t=int(input())
for i in range(t):
    lst=list(map(int,input().split()))
    rainy=0
    summer=0
    for j in lst:
        
        if(j==0):
            rainy+=1
        else:
            summer+=1
    if(rainy>summer):
        print("No")
    else:
        print("Yes")