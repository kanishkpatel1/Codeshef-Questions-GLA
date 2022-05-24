t=int(input())
lst2=[]
for i in range(t):
  sumeven=sumodd=0
  n=int(input())
  lst=list(map(int,input().split()))
  for j in range(n):
    if(j%2==0):
      sumeven+=lst[j]
    else:
      sumodd+=lst[j]
  if(sumeven>sumodd):
    print(sumeven)
  else:
    print(sumodd)
    