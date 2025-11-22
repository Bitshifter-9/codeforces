t=int(input())
for i in range(t):
    n=int(input())
    if n==1:
        print(0)
    else:
        cou_3=0
        while n>0 and n%6==0:
            n=n//6
            cou_3+=1
        cou_2=0
        while n>0 and n%2==0:
            cou_2+=1
            n=n//2
        if n>1 or cou_2>cou_3:
            print(-1)
        else:
            print(2*cou_3-cou_2)
            #     print(-1)
            