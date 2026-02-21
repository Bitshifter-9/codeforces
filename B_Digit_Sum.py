n,k=map(int,input().split())
cou=0
for io in range(n+1):
    s=str(io)
    ip=0
    for po in s:
        ip+=int(po)
    if ip==k:
        cou+=1
print(cou)
