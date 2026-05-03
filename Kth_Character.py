# cook your dish here
t=int(input())
se=set()
for k in range(1000):
    se.add(2**k)
for i in range(t):
    n=int(input())
    def x(i,j):
        if i==1:
            return "a"
        if i in se:
            if j==1:

                return "a"
            return "c"
        x()
        

print(se)
        
        