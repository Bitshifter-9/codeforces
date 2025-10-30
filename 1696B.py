t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    cou=0
    ans=True
    for j in range(n):
        if lis[j]!=0:
            if ans:
             
                cou+=1
                ans=False
        else:
            ans=True
    if cou>=2:
        print(2)
    else:
        
        print(cou)

