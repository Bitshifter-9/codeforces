t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    a=[]
    b=[]
    for j in range(n):
        if s[j]=="a":
            a.append(j)
        else:
            b.append(j)
    # print(a,b)
    cou=-1
    cou_2=-1
    if len(a)>0:
        on=a[len(a)//2]
        cou=0
        # print(on)
        for k in range(len(a)):
            if a[k]!=on:
                if a[k]<on:
                    cou+=abs(on-a[k]-1)
                else:
                    cou+=abs(on-a[k]+1)
    if len(b)>0:
        cou_2=0
        on_2=b[len(b)//2]
        for k in range(len(b)):
            if b[k]!=on_2:
                if b[k]<on_2:
                    cou_2+=abs(on_2-b[k]-1)
                else:
                    cou_2+=abs(on_2-b[k]+1)
            
            # print(cou)
    if cou!=-1 and cou_2!=-1:   
        print(min(cou,cou_2))
    else:
        print(0)