t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    cou_a_o=a.count(1)

    cou_a_z=a.count(0)

    cou_b_o=b.count(1)
    cou_b_z=b.count(0)
    for j in range(n):
        if j%2==0:
            if a[j]!=b[j] and cou_a_o%2==0:
                if a[j]==1:
                    a[j]=0
                    b[j]=1
                    cou_a_z+=1
                    cou_a_o-=1
                    cou_b_o+=1
                    cou_b_z-=1
                else:
                    a[j]=1
                    b[j]=0
                    cou_a_z-=1
                    cou_a_o+=1
                    cou_b_o-=1
                    cou_b_z+=1
        else:
            if cou_b_o%2==0 and a[j]!=b[j]:
                if b[j]==1:
                    b[j]=0
                    a[j]=1
                    cou_b_z+=1
                    cou_b_o-=1
                    cou_a_o+=1
                    cou_a_z-=1
                else:
                    b[j]=1
                    a[j]=0
                    cou_b_z-=1
                    cou_b_o+=1
                    cou_a_o-=1
                    cou_a_z+=1
    # print(a,b)
    # print(cou_a_o,cou_b_o)
    if cou_a_o%2!=0:
        ans1=1
    else:
        ans1=0
    if cou_b_o%2!=0:
        ans2=1
    else:
        ans2=0
    if ans1>ans2:
        print("Ajisai")
    elif ans1<ans2:
        print("Mai")
    else:
        print("Tie")
    # print(ans1,ans2)

                    

