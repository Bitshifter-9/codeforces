n,y=map(int,input().split())
lis=list(map(int,input().split()))
# lis.sort()
dic={}

for i in lis:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
ans=True
for j in range(1,y):
    if j not in dic:
        continue
    
    x=dic[j]
    if x%(j+1)!=0:
        ans=False
        break
    z=x//(j+1)
    if j+1 in dic:
        dic[j+1]+=z
    else:
        dic[j+1]=z
    dic[j] %= (j+1)

if ans:
    if y in dic:
        if dic[y] >0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")


