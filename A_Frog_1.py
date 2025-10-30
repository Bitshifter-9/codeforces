n=int(input())
lis=list(map(int,input().split()))
m={}
def x(i):
    if i>=n-1:
        return 0
    if i in m:
        return m[i]    
    one = -1
    two = -1
    if i+1<n:

        one=abs(lis[i]-lis[i+1])+x(i+1)
    if i+2<n:
        two=abs(lis[i]-lis[i+2])+x(i+2)
    if one!=-1 and two!=-1:
        m[i]=min(one,two)
    elif one!=-1 and two==-1:
        m[i]=one
    return m[i]
if len(lis)>=2:
    print(x(0))
else:
    print(0)
# ans=[]
# def x(i,cu):
#     if i==n-1:
#         ans.append(sum(cu))
#         # print(cu)
#         return
#     if i+1<n:
#         x(i+1,cu+[abs(lis[i]-lis[i+1])])
#     if i+2<n:
#         x(i+2,cu+[abs(lis[i]-lis[i+2])])
# x(0,[])
# print(min(ans))