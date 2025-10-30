t=int(input())
for i in range(t):
    x,k=map(int,input().split())
    cou=0
    num=x
    su_m=0
    lis=[]
    while su_m!=x:
        if num%k==0:
            num-=1
        else:
            su_m+=num
            cou+=1
    
            lis.append(num)
            if x-su_m%k!=0 and su_m!=x:
                
                
                lis.append(x-su_m)
                cou+=1
                su_m=x
            num-=1
    print(cou)
    print(*lis)

