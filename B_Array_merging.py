t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    dic_1={}
    dic_2={}
    cou=1
    for j in range(n-1):
        if a[j]==a[j+1]:
            cou+=1
        else:
            if a[j] in dic_1:
                dic_1[a[j]]=max(cou,dic_1[a[j]])
            else:
                dic_1[a[j]]=cou
            cou=1
    if a[-1] in dic_1:
        dic_1[a[-1]]=max(dic_1[a[-1]],cou)
    else:
        dic_1[a[-1]]=cou
    cou_2=1
    for j in range(n-1):
        if b[j]==b[j+1]:
            cou_2+=1
        else:
            if b[j] in dic_2:
                dic_2[b[j]]=max(dic_2[b[j]],cou_2)
            else:
                dic_2[b[j]]=cou_2
            
            cou_2=1
    if b[-1] in dic_2:
        dic_2[b[-1]]=max(cou_2,dic_2[b[-1]])
    else:
        dic_2[b[-1]]=cou_2
    ma=0
    for k in dic_1:
        if k in dic_2:
            ma=max(ma,dic_1[k]+dic_2[k])
        else:
            ma=max(ma,dic_1[k])
    for o in dic_2:
        if o in dic_1:
            ma=max(ma,dic_2[o]+dic_1[o])
        else:
            ma=max(ma,dic_2[o])
    print(ma)
            


