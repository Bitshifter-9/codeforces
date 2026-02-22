t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    cou_0=s.count("0")
    cou_1=n-cou_0
    if cou_0==n:
        print(0)
    elif cou_0%2==0 and cou_1%2!=0:
        print(-1)
    else:
        ans=[]
        if cou_1%2==0:
            for k in range(n):
                if s[k]=="1":
                    ans.append(k+1)
        else:
            for k in range(n):
                if s[k]=="0":
                    ans.append(k+1)
        print(len(ans))
        print(*ans)

