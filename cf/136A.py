# t=int(input())
# lis=list(map(int,input().split()))
# x=[]
# for i in range(t):
#     x.append([lis[i],i+1])
# x.sort()
# # print(x)
# for j in range(t):
#     print(x[j][1],end=" ")
ans=-1
a=1
b=2
def f(x):
    return x**2 - 2
epsilon = 1e-6

while (b-a)>epsilon :
    mid=(a+b)/2
    if f(mid)==0:
        ans=mid
        break
    elif f(mid)<0:
        a=mid
    else:
        b=mid
    ans=mid
    # print(a,b)
print(ans)