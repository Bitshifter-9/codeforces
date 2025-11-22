t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    
    ans1=0
    ans2=0
    for j in range(n):
        if j%2==0:
            a1=ans1^a[j]
            b1=ans2^b[j]
            a2=ans1^b[j]
            b2=ans2^a[j]
        
            if a1-b1 >= a2-b2:
                ans1=ans1^a[j]
                ans2=ans2^b[j]
            else:
                ans1=ans1^b[j]
                ans2=ans2^a[j]
        else:
            a1=ans1^a[j]
            b1=ans2^b[j]
            a2=ans1^b[j]
            b2=ans2^a[j]
      
            if b1-a1 >= b2-a2:
                ans1=ans1^a[j]
                ans2=ans2^b[j]
            else:
                ans1=ans1^b[j]
                ans2=ans2^a[j]
    if ans1>ans2:
        print("Ajisai")
    elif ans2>ans1:
        print("Mai")
    else:
        print("Tie")