def x(n):
    if n<=0:
        return 0
    print(n)
    x(n-1)
    print(n)
    x(n-2)
    print(n)
x(4)