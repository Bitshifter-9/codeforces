t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    lis.sort()
    cou_o=lis.count(1)
    cou_t=lis.count(-1)
    cou=0
    while cou_t%2!=0 or cou_o<cou_t:
        lis.append(1)
        lis.pop(0)
        cou+=1
        cou_o=lis.count(1)
        cou_t=lis.count(-1)
    print(cou)



    

