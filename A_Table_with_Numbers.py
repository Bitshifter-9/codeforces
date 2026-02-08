t=int(input())
for i in range(t):
    n,h,l=map(int,input().split())
    lis=list(map(int,input().split()))
    arr=[]
    lis.sort(reverse=True)
    z=max(h,l)
    c1=0
    c2=0
    for j in lis:
        if j<=z :
            c1+=1
        if j<=min(h,l):
            c2+=1
    l=c1-c2
    ans=min(l,c2)
    x=(c2-ans)//2
    print(ans+x)

    
    
      
    # arr.sort()
    # cou=0
    # left=0
    # right=len(arr)-1
    # m=min(l,h)
    # cou=0
    # # print(arr)
    # while left<right:
    #     if arr[left]<=m and arr[right]<=z:
    #         cou+=1
    #         left+=1
    #         right-=1
    #     elif arr[right]>z:
    #         right-=1
    #     elif arr[left]>m:
    #         break
    # print(cou)

        
    # print(len(arr)//2)
