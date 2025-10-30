t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    lis=list(map(int,input().split()))
    if lis==sorted(lis):
        print("YES")
    else:
        if k>1:
            print("YES")
        else:
            print("NO")xx