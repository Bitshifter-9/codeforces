t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    ans=[]
    def x(s,c):
        if len(s)==1:
            if s[0]==c:
                return 0
            return 1
        mid=len(s)//2
        c_1=(mid - s[:mid].count(c))+x(s[mid:],chr(ord(c)+1))
        c_2=(mid-s[mid:].count(c))+x(s[:mid],chr(ord(c)+1))
        return min(c_1,c_2)
    print(x(s,"a"))





        

        



            
