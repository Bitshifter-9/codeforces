t=int(input())
for i in range(t):
    n=int(input())
    x=n//4
    y=n//6
    ma_x=x+(n-(4*x))/6
    mi_n=y+(n-(6*y))/6
    print(mi_n,ma_x)