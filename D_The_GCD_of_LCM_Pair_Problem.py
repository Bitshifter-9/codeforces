n=int(input())
lis=list(map(int,input().split()))
z=max(lis)+1
spf=list(range(z))
pri=[]
for i in range(2,z):
    if spf[i]==i:
        pri.append(i)
        for j in range(2*i,z,i):
            if spf[j]==j:
                spf[j]=i

first={}
second={}
cn={}
for x in lis:
    cur={}
    while x>1:
        p=spf[x]
        if p in cur:
            cur[p]+=1
        else:
            cur[p]=1
        x//=p
    for z in cur:
        if z in cn:
            cn[z]+=1
        else:
            cn[z]=1
            first[z]=float("inf")
            second[z]=float("inf")
        if cur[z]<first[z]:
            second[z]=first[z]
            first[z]=cur[z]
        elif cur[z]<second[z]:
            second[z]=cur[z]
ans=1
# print(second,first)
for mp in cn:
    if cn[mp]==n:
        ans*=mp**second[mp]
    elif cn[mp]==n-1:
        ans*=mp**first[mp]
    else:
        ans*=1
print(ans)

# m={}
# se=set()
# def fac(m):
   
#     while m>1:
#         se.add(spf[m])
#         m//=spf[m]
#     return se
# def fact(el):
#     dic={}
#     while el>1:
#         lp=spf[el]
#         if lp in dic:
#             dic[lp]+=1
#         else:
#             dic[lp]=1
#         el=el//lp
#     for iu in se:
#         if iu not in dic:
#             dic[iu]=0
#     for jp in dic:
#         if jp in m:
#             m[jp].append(dic[jp])
#         else:
#             m[jp]=[dic[jp]]
# for ioi in lis:
  
#     fac(ioi)
# for io in lis:
  
#     fact(io)
# ans=1
# for las in m:
#     che=m[las]
#     che.sort()
#     # print(las,che)
#     if len(che)>=2:
       
#         ans*=(las**che[1])
#     else:
#         ans*=(las**0)
# print(ans)
# # print(2*27)





