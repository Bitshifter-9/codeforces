n=int(input())

def x(i):
    if i==n:
        return
    
    x(i+1)
    print(i)
x(0)
    