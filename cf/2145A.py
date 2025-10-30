t=int(input())
for i in range(t):
    n=int(input())
    x=n//3
    if n!=3*x:
        print((x+1)*3-n)
    else:
        print(0)
