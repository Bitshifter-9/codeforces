n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    a[i]=a[i]-1
r=[0]*n
for i in range(n-1,-1,-1):
    if a[i]==i:
        r[i]=i
    else:
        r[i]=r[a[i]]
for i in range(n):
    r[i]=r[i]+1
for i in range(n):
    print(r[i],end=" ")

