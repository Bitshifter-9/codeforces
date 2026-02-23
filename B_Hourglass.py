t = int(input())
for _ in range(t):
    s, k, m = map(int, input().split())
    tu=m//k
    ex=0
    if m>k:
        ex=m%k
    if m<k:
        print(max(0,s-m))
   
    
  
    elif tu%2==0:
        print(max(0,s-ex))
    else:
        print(max(0,min(k,s)-ex))

     