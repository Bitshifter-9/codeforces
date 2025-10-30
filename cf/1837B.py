t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    lis=[1]
    m=1
    cou=0
    ma=0
    cou_1=0
    ma_1=0
    for j in range(n):
        if s[j]=="<":
            m+=1
            lis.append(m)
            cou+=1
        else:
            ma=max(ma,cou)
            cou=0
    ma=max(ma,cou)
    for j in range(n):
        if s[j]==">":
            m+=1
            lis.append(m)
            cou_1+=1
        else:
            ma_1=max(ma_1,cou_1)
            cou_1=0
    ma_1=max(ma_1,cou_1)
    # print(lis)
   
    
    print(max(ma,ma_1)+1)


    
    
            
