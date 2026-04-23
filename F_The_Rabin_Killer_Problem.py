
import math

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
if n==1:
    print(1)
elif c(n):
    print(2)
else:
    z=10**6+1
    spf=list(range(z))
    pri=[]
    for k in range(2,z):
        if spf[k]==k:
            pri.append(k)
            for j in range(2*k,z,k):
                if spf[j]==j:
                    spf[j]=k
    temp=n
    m={}
    for p in pri:
        if p*p>temp:
            break
        if temp%p==0:
            cou=0
            while temp%p==0:
                temp//=p
                cou+=1
            m[p]=cou
    
    if temp>1:
        r=int(math.isqrt(temp))
        if r*r==temp and c(r):
            if r in m:
                m[r]+=2
            else:
                m[r]=2
        elif c(temp):
            if temp in m:
                m[temp]+=1
            else:
                m[temp]=1
        else:
            ans=1
            for jp in m:
                ans*=(m[jp]+1)
            ans*=4
            print(ans)
            exit()
    
    ans=1
    for jp in m:
        ans*=(m[jp]+1)
    print(ans)
