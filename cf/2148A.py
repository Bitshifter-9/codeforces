t=int(input())
for i in range(t):
    x,n=map(int,input().split())
    ans=[]
    for j in range(n):
        if j%2==0:
            ans.append(x)
        else:
            ans.append(-x)
    print(sum(ans))