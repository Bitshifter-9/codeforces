t=int(input())
for i in range(t):
    n=int(input())
    if n==1:
        print(1)
        print(1)
    elif n==2:
        print(2)
        print(2,1)
    else:
        x=[]
        pow=0
        while 2**pow<n:
            x.append(2**pow)
            pow+=1
        a=[n]
        num=n
        z=(bin(n)[2:])    
        re=[]
        for k in z:
            re.append(k)
        j=len(re)-1
        pre=n
        while pre-(2**(len(re)-j-1))!=x[-1] and j>=0 :
            if re[j]=="1":
                pre=pre-(2**(len(re)-j-1))
                a.append(pre)
            j-=1
        # print(a,x)
        x.reverse()
        op=a+x
        print(len(op))
        print(*op)
        # x.reverse()
        # if a[-1]==0:
        #     a=a[:-1]
        # fi=a+x[1:]
        # print(len(fi))
        # print(a,x)
        


