t=int(input())
for i in range(t):
    odd=[]
    eve=[]
    n=int(input())
    lis=list(map(int,input().split()))
    for j in range(n):
        if lis[j]%2==0:
            eve.append(lis[j])
        else:
            odd.append(lis[j])
    ans=0
    if len(odd)==0:
        print(0)
    else:
        
        odd.sort()
        if len(odd)%2==0:
            odd=odd[1:]
        odd1=odd[:len(odd)//2]
        odd2=odd[len(odd)//2:]
        ans=sum(eve)+sum(odd2)
        print(ans)