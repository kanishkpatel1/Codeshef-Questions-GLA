n=int(input())
for i in range (n):
    (a, b, c) = map(int, input().split(' '))
    lst=[a,b,c]
    b=sorted(lst)
    print(b[-2])