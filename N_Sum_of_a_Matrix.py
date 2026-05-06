n,m=map(int,input().split())
oq=[]
for k in range(n):
    row_1=list(map(int,input().split()))
    oq.append(row_1)
op=[]
for z in range(n):
    row_1=list(map(int,input().split()))
    op.append(row_1)
ans=[]
for iq in range(n):
    iu=[]
    for ip in range(m):
        iu.append(op[iq][ip]+oq[iq][ip])
    print(*iu)