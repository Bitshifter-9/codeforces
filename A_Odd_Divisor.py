t=int(input())
for i in range(t):
    n=int(input())
    cou=0
    ans=False
    if n%2!=0:
        print("YES")
    else:
        while n%2==0 and n>0:
            n=n//2
        if n==1:
            print("NO")
        else:
            print("YES")