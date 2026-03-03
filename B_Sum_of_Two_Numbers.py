t=int(input())
for i in range(t):
    n=int(input())
    z=str(n)
    x=[]
    y=[]
    ans=False
    for j in z:
        op=int(j)//2
        qp=int(j)-op
        if int(j)%2==0:
            x.append(str(op))
            y.append(str(qp))
        else:
            if ans:
                x.append(str(op))
                y.append(str(qp))
                ans=False
            else:
                x.append(str(qp))
                y.append(str(op))
                ans=True
    nu1="".join(x)
    num2="".join(y)
    print(int(nu1),int(num2))



# m=234

