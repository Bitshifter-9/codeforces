t=int(input())
import math
for i in range(t):
    ans1=False
    ans2=False
    n=int(input())
    if n%2!=0 or n<4:
        print(-1)
    else:
        print(math.ceil(n/6),n//4)

