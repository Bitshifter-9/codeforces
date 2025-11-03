t=int(input())
for i in range(t):
    n=int(input())
    s,t=map(str,input().split())
    lis=[]
    arr=[]
    for i in range(n):
        lis.append(s[i])
        arr.append(t[i])
    lis.sort()
    arr.sort()
    if lis==arr:
        print("YES")
    else:
        print("NO")

