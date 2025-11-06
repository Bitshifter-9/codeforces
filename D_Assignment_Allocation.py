
t=int(input())
for _ in range(t):
    n,d,k=map(int,input().split())
    x=[]
    arr=[0]*(d+1)
    for i in range(n):
        a,b=map(int,input().split())
        x.append([a,b])
    s= sorted(x, key=lambda x: (x[0],x[1]))
    day=1
    cou=0
    print(s)
    for i in range(len(s)):
        if s[i][1]<day:
            cou+=1
        else:
            day+=1
    print(cou-k)

