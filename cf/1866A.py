n=int(input())
lis=list(map(int,input().split()))
mi_n=abs(lis[0])
for i in lis:
    mi_n=min(mi_n,abs(i))
print(mi_n)
