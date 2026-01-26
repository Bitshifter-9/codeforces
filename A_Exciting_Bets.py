t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if b>a:
        a,b=b,a
    if a==b:
        print(0,0)
    else:
        print((a-b),(min(b%(a-b),((a-b)-b)%(a-b))))