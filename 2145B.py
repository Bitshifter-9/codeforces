from collections import deque 
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    num=k
    s=input()
    one=0
    tow=0
    zero=0  
    for p in s:
        if p=="0":
            zero+=1
 
        elif p=="1":

            one+=1
        else:
    
            tow+=1
    if n==1:
        print("-")
    else:
        left=zero+tow
        res = []
        for o in range(1, n+1):
            if o-1 < o-(n-k):
                res.append("-")
                continue
            elif o-(n-k) <= zero and o-1 >= zero+tow:
                res.append("+")
            elif o-(n-k) > zero+tow or o-1 < zero:
                res.append("-")
            else:
                res.append("?")
        print("".join(res))      

 
    
 
 