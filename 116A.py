n=int(input())
cou=0
ma=0
for i in range(n):
    a,b=map(int,input().split())
    cou-=a
    cou+=b
    ma=max(ma,cou)
print(ma)