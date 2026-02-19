t=int(input())
for i in range(t):
    n=int(input())
    z=str(n)
    arr=[]
    for k in z:
        arr.append(int(k))
    z=arr[0]
    
    arr[0]-=1
    # arr=arr[1:]
    arr.sort(reverse=True)
    cou=0
    ans=sum(arr)+1
    # print(ans,arr)
    while ans>=10 and cou<n:
        ans-=arr[cou]
        cou+=1
    print(cou)