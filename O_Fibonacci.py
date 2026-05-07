n=int(input())
def x(n):
    if n<=1:
        return 0
    if n==2:
        return 1
    
    
    
    return x(n-1)+x(n-2)
print(x(n))