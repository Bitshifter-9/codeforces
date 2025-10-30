t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    s=input()
    cou_odd=0
    lis=[]
    for j in s:
        lis.append(j)
    m=set(lis)
    for l in m:
        if lis.count(l)%2!=0:
            cou_odd+=1
    # print(cou_odd)
    cou_eve=len(m)-cou_odd
    if cou_odd-k<=1:
        print("YES")
    else:
        print("NO")
    