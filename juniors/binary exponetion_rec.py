t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    def bina(a,b):
        if b==0:
            return 1
        half=bina(a,b//2)
        if b%2==1:
            return (a*half*half)%(10**9+7)
        else:
            return (half*half)%(10**9+7)
    print(bina(a,b))