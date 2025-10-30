t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if a!=max(a,b,c) and a!=min(a,b,c):
        print(a)
    elif b!=max(a,b,c) and b!=min(a,b,c):
        print(b)
    else:
        print(c)