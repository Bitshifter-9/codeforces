import math
t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    ma=0
    num=-1
    lis.sort()
    cou=1
    # print(lis)
    for k in range(n-1):
        if lis[k]==lis[k+1]:
            cou+=1
            # print(cou)
        else:
            if cou>ma:
                num=lis[k]
               
                ma=max(cou,ma)
            cou=1
    
    if cou>ma:
        num=lis[-1]
        ma=max(cou,ma)
    # print(ma)
    if num==-1:
        ma=1
    # else:
    #     ma+=1   
    ope=0
    while ma<n:   
        ope+=1            
        if ma*2<=n:
            ope+=ma
            ma*=2
      
        else:
            ope+=n-ma
            ma=n            
    print(ope)
    