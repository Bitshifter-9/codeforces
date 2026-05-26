t=int(input())
for _ in range(t)
a,b=map(int,input().split())
re=1
while b>0:
    if b%2==1:
        re=(re*a)%(10**9+7)
    a=(a*a)%(10**9+7)

    b//=2
    # print(a,b,re)
print(re)

        
