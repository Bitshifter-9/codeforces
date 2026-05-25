def gcd(x1,y1):
    if x1%y1==0:
        return y1
    return gcd(y1,(x1%y1))
print(gcd(25,60))
