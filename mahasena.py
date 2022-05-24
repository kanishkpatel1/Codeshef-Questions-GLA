a=int(input())
b= list(map(int, input().split(' ')))
c=d=0
for i in range(len(b)):
    if(b[i]%2==0):
        c+=1
    else:
        d+=1
if(c>d):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
