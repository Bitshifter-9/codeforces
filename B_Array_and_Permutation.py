t=int(input())
for _ in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    ans=True
    for i in range(n):
        if arr[i]!=lis[i]:
            ans=False
            if i>0:
                if lis[i-1]==arr[i]:
                    lis[i]=arr[i]
                    ans=True




