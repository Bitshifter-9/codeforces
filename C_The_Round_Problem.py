t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    temp=n
    cou_2=0
    while temp%2==0:
        cou_2+=1
        temp//=2
    cou_5=0
    while temp%5==0:
        cou_5+=1
        temp//=5
    k=1
    while cou_2<cou_5 and k*2<=m:
        k*=2
        cou_2+=1
    while cou_2>cou_5 and k*5<=m:
        cou_5+=1
        k*=5
    while k*10<=m:
        k*=10
    # k*=m//k
    print(n*k*(m//k))

    
        

