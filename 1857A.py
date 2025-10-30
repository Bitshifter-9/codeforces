t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    cou_eve=0
    cou_odd=0
    if sum(lis)%2==0:
        print("YES")
    else:
        print("NO")