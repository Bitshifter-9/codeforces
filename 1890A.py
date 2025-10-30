t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    ans="Yes"
    cou=0
    x=set(lis)
    if len(x)>2:
        ans="No"
    else:
        arr=list(x)
        if len(arr)==2:
            if abs(lis.count(arr[0])-lis.count(arr[1]))>1:
                ans="No"
    print(ans)