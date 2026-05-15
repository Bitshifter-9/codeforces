t=int(input())
for i in range(t):
    n=int(input())
    x=n
    while x%20==0 or x%10==0:
        if x%20==0 and x%10==0:
            if x//20==1:
                x//=20
            else:
                x//=10

        if x%20==0:
            x//=20
        else:
            x//=10
    if x==1:
        print("YES")
    else:
        print("NO")

