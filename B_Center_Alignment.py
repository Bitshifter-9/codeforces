n=int(input())
arr=[]
k=0
for j in range(n):
    s=input()
    k=max(k,len(s))
    arr.append(s)
lis=[]
for m in arr:
    q=len(m)
    ip=k-q
    print(("."*(ip//2))+m+("."*(ip//2)))


