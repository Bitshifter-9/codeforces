t=int(input())
for i in range(t):
    ans1=False
    ans2=False
    n=int(input())
    cou_1=0
    a=n//6
    cou_1+=a
    remia=n-(a*6)
    if remia%4==0:
        ans1=True
    cou_1+=remia//4
    cou_2=0
    b=n//4
    cou_2+=b
    rema=n-(4*b)
    if rema%6==0:
        ans2=True
    cou_2+=rema//6
    print(cou_1,cou_2,ans1,ans2,remia,rema)

    if cou_1==cou_2 and cou_2==0:
        print(-1,-1)
    elif ans1 and ans2:

        print(cou_1,cou_2)
    elif ans1:
        print(cou_1,cou_1)
    elif ans2:
        print(cou_2,cou_2)
    else:
        print(-1)

