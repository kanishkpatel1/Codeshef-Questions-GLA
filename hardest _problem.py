t=int(input())
for i in range(t):
    (sa,sb,sc)=map(int,input().split())
    if((sa<sb) and (sa<sc)):
        print("Draw")
    elif((sb<sa) and (sb<sc)):
        print("Bob")
    else:
        print("Alice")