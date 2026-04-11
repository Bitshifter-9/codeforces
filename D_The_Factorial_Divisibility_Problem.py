import sys
sys.setrecursionlimit(10**9)
n,y=map(int,input().split())
lis=list(map(int,input().split()))
lis.sort()
# print(lis)
cou=0
ans=True
for i in range(n-1):
    # print(lis[i])
    if lis[i]==lis[i+1]:
        cou+=1
    else:
        if cou==lis[i] and lis[i+1]==lis[i]+1:
            cou=1
        else:
           
            ans=False
            break
if ans:
    if cou==lis[-1]:
        z=lis[-1]+1
        if z>=y:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")


