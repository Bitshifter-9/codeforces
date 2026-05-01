import math
k=int(input())
arr=[]
m=1
for i in range(k):
    n=int(input())
    if i<k-2:
        arr.append(n)
        m*=math.factorial(n)
    else:
        arr.append(n-1)
        m*=math.factorial(n-1)
    # print(n)
z=math.factorial(sum(arr))

print((z//m)%(10**9+7))






        
        