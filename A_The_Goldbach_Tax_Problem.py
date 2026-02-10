def c(n):
    if n < 2:
        return False

    small_primes = [2,3,5,7,11,13,17,19,23,29]
    for p in small_primes:
        if n % p == 0:
            return n == p
    d=n-1
    s=0
    while d%2==0:
        s+=1
        d//=2
    def check(a):
        x=pow(a,d,n)
        if x==1 or x==n-1:
            return True
        for i in range(s-1):
            x=(x*x)%n
            if x==n-1:
                return True
        return False
    bases = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    for a in bases:
        if a%n==0:
            continue
        if not check(a):
            return False
    return True
n=int(input())
if c(n):
    print(1)
elif n%2==0:
    print(2)
elif c(n-2):
    print(2)
else:
    print(3)