t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    for k in range(n):
        if lis[k]==1:
            lis[k]=lis[k]+1
    
    for j in range(n-1):
       
        if lis[j+1]%lis[j]==0:
            lis[j+1]=lis[j+1]+1
    print(*lis)
            
