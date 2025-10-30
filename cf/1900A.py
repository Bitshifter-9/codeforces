t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    cou=0
    ma=0
    lis=[]
    coud=0
    for j in range(n-1):
        if s[j]==s[j+1] and s[j]=='.':
            cou+=1
            lis.append(j)
            
        else:
            ma=max(ma,cou)
            cou=0
        if s[j]=='.':
            coud+=1
    if s[-1]=='.':
        coud+=1
    ma=max(cou,ma)
    if ma>=2:
        print(2)
    else:
        print(coud)

