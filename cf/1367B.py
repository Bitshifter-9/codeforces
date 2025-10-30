t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    cou_eve=0
    not_pop=0
    cou=0
    for i in range(n):
        if lis[i]%2==0 and i%2==0:
            cou_eve+=1
        if lis[i]%2==0:
            cou+=1
    cou_odd=n-cou
    if cou_odd==cou and n%2==0:
        print(cou-cou_eve)
    elif cou-cou_odd==1 and n%2!=0:
        print(abs(cou-cou_eve))
    else:
        print(-1)
