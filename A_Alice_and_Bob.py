t=int(input())
for i in range(t):
    n,a=map(int,input().split())
    lis=list(map(int,input().split()))
    cou_1=0
    cou_2=0
    for j in range(len(lis)):
        if lis[j]>=a:
            cou_1+=1
        else:
            cou_2+=1
    if cou_1>cou_2:
        print(a+1)
    else:
        print(a-1)
    # print(cou_1,cou_2)