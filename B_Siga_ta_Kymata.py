t=int(input())
for i in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    s=input()
    if s[0]=="1" or s[-1]=="1" or s[lis.index(1)]=="1" or s[lis.index(n)]=="1":
        print(-1)
    else:
        print(5)
        print(1,lis.index(1)+1)
        print(1,lis.index(n)+1)
        print(lis.index(1)+1,n)
        print(lis.index(n)+1,n)
        
        print(min(lis.index(1)+1,lis.index(n)+1),max(lis.index(1)+1,lis.index(n)+1))
       
       