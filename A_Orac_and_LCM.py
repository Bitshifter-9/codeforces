# Your code here
t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    dic={
        2:1,
        4:2,
        6:1,
        8:3,
        10:1,
        12:2,
        14:1

    }
    mp={
        2:1,
        4:1,
        6:3,
        8:1,
        10:5,
        12:3,
        14:7
        
    }
    lis.sort()
    ind=-1
    for j in range(n-1,-1,-1):
        if lis[j]%2!=0:
            ind=j
            break
    # print(ind )
    if ind==-1:
        ind=n-1
   
    for k in range(n):
        if  lis[k] in dic and k!=ind:
            lis[ind]=lis[ind]*(2**dic[lis[k]])
            lis[k]=mp[lis[k]]
            
            
    print(sum(lis))