t=int(input())
for i in range(t):
    n,q=map(int,input().split())
    lis=list(map(int,input().split()))
    arr=[0]
    su=0
    for j in lis:
        su+=j
        arr.append(su)
    # print(arr)
    for w in range(q):
        l,r,k=map(int,input().split())
        x=arr[-1]-(arr[r]-arr[l-1])+((r-l+1)*k)
        if x%2!=0:
            print("YES")
        else:
            print("NO")
