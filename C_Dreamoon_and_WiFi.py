from math import factorial
s=input()
z=input()
plus=0
minus=0
ques=0
pl=0
mi=0
qu=0

for i in s:
    if i=="+":
        plus+=1
    elif i=="-":
        minus+=1
    else:
        ques+=1
for j in z:
    if j=="+":
        pl+=1
    elif j=="-":
        mi+=1
    else:
        qu+=1

if pl==plus and minus==mi:
    print(f"{1:.12f}")
else:
    if qu==0:
        print(f"{0:.12f}")
    else:
        if minus-mi<0 or plus-pl<0:
            print(f"{0:.12f}")
        else:
            if plus+minus-(pl+mi+qu)==0:
                x=plus-pl
                y=minus-mi
                ans=factorial(x+y)/(factorial(x)*factorial(y))
                print(f"{ans/2**qu:.12f}")
            else:
                print(f"{0:.12f}")


     

