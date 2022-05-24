t=int(input())
for i in range (t):
    n=int(input())
    c=n
    a=str(n)
    sum=0
    for i in range (len(a)):
        a=n%10
        n=n//10
        sum+=a
    if(c%sum==0):
        print("Yes")
    else:
        print("No")
