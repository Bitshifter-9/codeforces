
nums=list(map(int,input().split()))
m={}
su=[]
def x(i,cur):
    if i>=len(nums):
      
        return sum(cur)
    if i in m:
        return m[i]
    a=x(i+1,cur)
    b=x(i+2,cur+[nums[i]])   
    m[i]=max(a,b)
    return m[i]    
print(x(0,[]))



m={}
su=[]
def x(i):
    if i>=len(nums):
      
        return 0
    if i in m:
        return m[i]
    a=x(i+1)
    b=nums[i]+x(i+2)   
    m[i]=max(a,b)
    return m[i]    
print(x(0))
    