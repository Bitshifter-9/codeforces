t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    if n%2==0:
        if k%4==1:
            print(n-k)
        elif k%4==2:
            print(n+1)
        elif k%4==3:
            print(n+k+1)
        else:
            print(n)
    else:
        if k%4==1:
            print(n+k)
        elif k%4==2:
            print(n-1)
        elif k%4==3:
            print(n-k-1)
        else:
            print(n)
