import sys
sys.setrecursionlimit(10**9)
def maxWeight(weights, values, W):
    m={}
    def x(i,weight):
        if weight<=0 or i>=len(weights):
            return 0
        
        if (i,weight) in m:
            return m[(i,weight)]
        ans=x(i+1,weight)
      
        if weights[i]<=weight:
            ans=max(ans,values[i]+x(i+1,weight-weights[i]))
           
            m[(i,weight)]=ans
        return ans
    return x(0,W)
n,W=map(int,input().split())
weights=[]
values=[]
for i in range(n):
    a,b=map(int,input().split())
    weights.append(a)
    values.append(b)
print(maxWeight(weights,values,W))
