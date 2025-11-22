t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    lis=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    c=list(map(int,input().split()))
    # c.sort(reverse=True)
    if len(c)>0:
        w=max(max(lis),max(c))
    else:
        w=max(lis)
    lis.sort(reverse=True)
    cou=0
    if max(lis)<min(arr):
        print(0)

    else:
        for j in range(len(arr)):
            if arr[j]>w:
                cou+=1
        ve=[]            
        for k in range(m):
            ve.append([c[k],arr[k]])
        ve.sort(key=lambda x : (-x[0],x[1]))
        # print(ve)
        index=0
        we=lis[0]
        # print(we)
        while index < len(ve) and ve[index][1]>we and ve[index][0]>0:
            index+=1
        if index == len(ve):
            index -= 1
        knife=max(we,ve[index][0])
        ind=0
        while ind < len(lis) and lis[ind]>ve[index][1]:
            ind+=1
        if ind == len(lis):
            ind -= 1
        knife_n=lis[ind]
        # print(knife,lis,ind,ve[index][0],knife_n)
        ans=0
        zero=[]
        for pr in range(len(ve)):
            if ve[pr][1]<=knife and ve[pr][0]!=0:
                ans+=1
            if ve[pr][0]==0:
                zero.append(ve[pr][1])
        zero.sort(reverse=True)
        left=0
        right=0
        cou=0
        while left<len(lis) and right<len(zero):
            if lis[left]>=zero[right]:
                ans+=1
                left+=1
                right+=1
            elif lis[left]<zero[right]:
                right+=1
        print(ans)
        
        





        # print(ve)






































# t=int(input())
# for i in range(t):
#     n,m=map(int,input().split())
#     lis=list(map(int,input().split()))
#     arr=list(map(int,input().split()))
#     c=list(map(int,input().split()))
#     w=max(max(lis),max(c))
#     lis.sort(reverse=True)
#     cou=0
#     if max(lis)<min(arr):
#         print(0)

#     else:
#         for j in range(len(arr)):
#             if arr[j]>w:
#                 cou+=1
#         ve=[]            
#         for k in range(m):
#             ve.append([c[k],arr[k]])
#         ve.sort(reverse=True)
#         co=0
#         index=0
#         we=max(lis)
#         print(ve)
#         while ve[index][1]>we and ve[index][0]>0:
#             index+=1
#         knife=max(we,ve[index][0])
#         zero=c.count(0)




#         # print(ve)
