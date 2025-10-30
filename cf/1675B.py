import math
t=int(input())
for i in range(t):
    n=int(input())
    cou=0
    lis=list(map(int,input().split()))
    for j in range(n-1,0,-1):
        if lis[j]==0:
            cou=-1
            break
     
        if lis[j-1]>lis[j] and lis[j]!=0:
            ans=math.log(lis[j-1]/lis[j])/math.log(2)
            if ans==math.ceil(ans):
                ans+=1
            else:
                ans=math.ceil(ans)
            cou+=ans
    
            lis[j-1]=lis[j-1]//(2**ans)
            
    
            
        elif lis[j-1]==lis[j] and lis[j]!=0:
            cou+=1
            lis[j-1]=lis[j-1]//2
        elif lis[j]==0:
            cou=-1
            break

    
        
            
    print(int(cou))


