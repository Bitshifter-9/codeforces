import math
n= int(input())
co=0
for i in range(1,n):
    if math.gcd(i,n-1)==1:
        co+=1
print(co)



