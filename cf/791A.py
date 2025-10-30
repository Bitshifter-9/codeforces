n,m=map(int,input().split())
cou=0
while n<=m:
    n*=3
    m*=2
    cou+=1
print(cou)