t= int(input())
for _ in range(t):
    n,m = map(int,input().split())
    arr = [int(x) for x in input().split()]
    count = 0
    for i in arr:
        if((i+m)%7==0):
            count+=1
    print(count)