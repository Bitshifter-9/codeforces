n=int(input())
for i in range(n):
    a,b=map(str,input().split())
    x=a[0]
    y=b[0]
    ans1=y+a[1:]
    ans2=x+b[1:]
    print(ans1,ans2)