n=int(input())
ans=5
cou=0

while n!=0:
    if ans<=(n):
        cou+=1
        n-=ans
    else:
        ans-=1
print(cou)