n=int(input())
for i in range(n):
    a=int(input())
    if(a%4==0):
        print("North")
    if(a%4==1):
        print("East")
    if(a%4==2):
        print("South")
    if(a%4==3):
        print("West")
